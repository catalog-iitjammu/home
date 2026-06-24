from fastapi import FastAPI, APIRouter, HTTPException, Query, Header, Depends, Request
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response, JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
import secrets
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, Optional, Any
import uuid

from seed_data import (
    NAV_TREE,
    CATALOG_VERSIONS,
    DEPARTMENTS,
    FACULTY_GROUPS,
    ACADEMIC_CALENDAR,
    FEES_DATA,
    INFO_PAGES,
)

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / ".env")

mongo_url = os.environ["MONGO_URL"]
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ["DB_NAME"]]

# --- Admin key (for state-changing endpoints) ---
ADMIN_API_KEY = os.environ.get("ADMIN_API_KEY", "").strip()
if not ADMIN_API_KEY:
    # Generate a strong default for first-run dev; print it once so the operator can grab it.
    # In production the operator MUST set ADMIN_API_KEY explicitly via env.
    ADMIN_API_KEY = secrets.token_urlsafe(32)
    logging.getLogger(__name__).warning(
        "ADMIN_API_KEY env var not set; generated ephemeral key: %s "
        "(set ADMIN_API_KEY in backend/.env to make it stable across restarts)",
        ADMIN_API_KEY,
    )


def require_admin(x_admin_key: Optional[str] = Header(None)):
    """FastAPI dependency: 401 if the X-Admin-Key header is missing/wrong."""
    if not x_admin_key or not secrets.compare_digest(x_admin_key, ADMIN_API_KEY):
        raise HTTPException(status_code=401, detail="Admin authentication required")
    return True


# --- Rate limiter ---
limiter = Limiter(key_func=get_remote_address, default_limits=["120/minute"])

app = FastAPI(title="IIT Jammu SmartCatalog API")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
api = APIRouter(prefix="/api")

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


# --- Security headers middleware ---
class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response: Response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = (
            "accelerometer=(), camera=(), geolocation=(), gyroscope=(), microphone=(), payment=()"
        )
        # Modest CSP suitable for an API; the SPA serves its own CSP.
        response.headers["Content-Security-Policy"] = (
            "default-src 'none'; frame-ancestors 'none'"
        )
        # HSTS only when served over HTTPS at the proxy level.
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        return response


# ---------- Models ----------
class Course(BaseModel):
    code: str = Field(..., min_length=1, max_length=20)
    title: str = Field(..., min_length=1, max_length=200)
    credits: int = Field(..., ge=0, le=20)
    hours: str = Field(..., min_length=1, max_length=20)
    desc: str = Field(..., min_length=1, max_length=1000)


class Department(BaseModel):
    slug: str
    code: str
    name: str
    description: str
    courses: List[Course]


class FacultyMember(BaseModel):
    name: str
    role: str
    email: str
    area: str


class FacultyGroup(BaseModel):
    slug: str
    title: str
    intro: str
    members: List[FacultyMember]


class CourseCreate(BaseModel):
    code: str = Field(..., min_length=1, max_length=20)
    title: str = Field(..., min_length=1, max_length=200)
    credits: int = Field(..., ge=0, le=20)
    hours: str = Field(..., min_length=1, max_length=20)
    desc: str = Field(..., min_length=1, max_length=1000)


# ---------- Helpers ----------
def _strip_mongo_id(doc: dict) -> dict:
    doc.pop("_id", None)
    return doc


# ---------- Seed (ADMIN ONLY) ----------
@api.post("/seed", dependencies=[Depends(require_admin)])
@limiter.limit("5/minute")
async def seed_database(request: Request, force: bool = False):
    """Seed the DB with initial IIT Jammu catalog content. Admin-only.

    Uses upsert semantics on `slug` keys; pass ?force=true to wipe and reseed.
    """
    if force:
        await db.departments.delete_many({})
        await db.faculty_groups.delete_many({})
        await db.calendar.delete_many({})
        await db.fees.delete_many({})
        await db.info_pages.delete_many({})
        await db.nav.delete_many({})
        await db.meta.delete_many({})

    for dept in DEPARTMENTS:
        await db.departments.update_one(
            {"slug": dept["slug"]}, {"$set": dept}, upsert=True
        )
    for fg in FACULTY_GROUPS:
        await db.faculty_groups.update_one(
            {"slug": fg["slug"]}, {"$set": fg}, upsert=True
        )
    for term in ACADEMIC_CALENDAR:
        await db.calendar.update_one(
            {"term": term["term"]}, {"$set": term}, upsert=True
        )
    for fee in FEES_DATA:
        await db.fees.update_one({"slug": fee["slug"]}, {"$set": fee}, upsert=True)
    for info in INFO_PAGES:
        await db.info_pages.update_one(
            {"slug": info["slug"]}, {"$set": info}, upsert=True
        )
    await db.nav.update_one(
        {"_id": "nav-tree"}, {"$set": {"tree": NAV_TREE}}, upsert=True
    )
    await db.meta.update_one(
        {"_id": "catalog-meta"},
        {"$set": {"versions": CATALOG_VERSIONS, "current": "Catalog 2024-25"}},
        upsert=True,
    )

    counts = {
        "departments": await db.departments.count_documents({}),
        "faculty_groups": await db.faculty_groups.count_documents({}),
        "calendar_terms": await db.calendar.count_documents({}),
        "fees": await db.fees.count_documents({}),
        "info_pages": await db.info_pages.count_documents({}),
    }
    return {"status": "ok", "force": force, "counts": counts}


async def _ensure_seeded():
    """Internal silent seed (no auth) used on startup / lazy-init only."""
    if await db.departments.count_documents({}) > 0:
        return
    for dept in DEPARTMENTS:
        await db.departments.update_one({"slug": dept["slug"]}, {"$set": dept}, upsert=True)
    for fg in FACULTY_GROUPS:
        await db.faculty_groups.update_one({"slug": fg["slug"]}, {"$set": fg}, upsert=True)
    for term in ACADEMIC_CALENDAR:
        await db.calendar.update_one({"term": term["term"]}, {"$set": term}, upsert=True)
    for fee in FEES_DATA:
        await db.fees.update_one({"slug": fee["slug"]}, {"$set": fee}, upsert=True)
    for info in INFO_PAGES:
        await db.info_pages.update_one({"slug": info["slug"]}, {"$set": info}, upsert=True)
    await db.nav.update_one({"_id": "nav-tree"}, {"$set": {"tree": NAV_TREE}}, upsert=True)
    await db.meta.update_one(
        {"_id": "catalog-meta"},
        {"$set": {"versions": CATALOG_VERSIONS, "current": "Catalog 2024-25"}},
        upsert=True,
    )


# ---------- Public read endpoints ----------
@api.get("/")
async def root():
    return {"message": "IIT Jammu SmartCatalog API", "version": "1.0"}


@api.get("/meta")
async def get_meta():
    await _ensure_seeded()
    doc = await db.meta.find_one({"_id": "catalog-meta"})
    if not doc:
        raise HTTPException(404, "Meta not found")
    return {
        "versions": doc.get("versions", []),
        "current": doc.get("current", "Catalog 2024-25"),
    }


@api.get("/nav")
async def get_nav():
    await _ensure_seeded()
    doc = await db.nav.find_one({"_id": "nav-tree"})
    if not doc:
        raise HTTPException(404, "Nav not found")
    return {"tree": doc["tree"]}


@api.get("/departments")
async def list_departments():
    await _ensure_seeded()
    docs = await db.departments.find().to_list(100)
    return [_strip_mongo_id(d) for d in docs]


@api.get("/departments/{slug}")
async def get_department(slug: str):
    await _ensure_seeded()
    doc = await db.departments.find_one({"slug": slug})
    if not doc:
        raise HTTPException(404, f"Department '{slug}' not found")
    return _strip_mongo_id(doc)


# ---------- Admin mutating endpoints ----------
@api.post(
    "/departments/{slug}/courses",
    dependencies=[Depends(require_admin)],
)
@limiter.limit("30/minute")
async def add_course(request: Request, slug: str, course: CourseCreate):
    await _ensure_seeded()
    dept = await db.departments.find_one({"slug": slug})
    if not dept:
        raise HTTPException(404, f"Department '{slug}' not found")
    if any(c.get("code") == course.code for c in dept.get("courses", [])):
        raise HTTPException(409, f"Course '{course.code}' already exists in {slug}")
    await db.departments.update_one(
        {"slug": slug}, {"$push": {"courses": course.dict()}}
    )
    return {"status": "ok", "added": course.code}


@api.delete(
    "/departments/{slug}/courses/{code}",
    dependencies=[Depends(require_admin)],
)
@limiter.limit("30/minute")
async def remove_course(request: Request, slug: str, code: str):
    res = await db.departments.update_one(
        {"slug": slug}, {"$pull": {"courses": {"code": code}}}
    )
    if res.modified_count == 0:
        raise HTTPException(404, "Course not found")
    return {"status": "ok", "removed": code}


# ---------- More public read endpoints ----------
@api.get("/faculty")
async def list_faculty():
    await _ensure_seeded()
    docs = await db.faculty_groups.find().to_list(100)
    return [_strip_mongo_id(d) for d in docs]


@api.get("/faculty/{slug}")
async def get_faculty_group(slug: str):
    await _ensure_seeded()
    doc = await db.faculty_groups.find_one({"slug": slug})
    if not doc:
        raise HTTPException(404, f"Faculty group '{slug}' not found")
    return _strip_mongo_id(doc)


@api.get("/calendar")
async def get_calendar():
    await _ensure_seeded()
    docs = await db.calendar.find().to_list(50)
    return [_strip_mongo_id(d) for d in docs]


@api.get("/fees")
async def list_fees():
    await _ensure_seeded()
    docs = await db.fees.find().to_list(50)
    return [_strip_mongo_id(d) for d in docs]


@api.get("/fees/{slug}")
async def get_fee(slug: str):
    await _ensure_seeded()
    doc = await db.fees.find_one({"slug": slug})
    if not doc:
        raise HTTPException(404, f"Fee section '{slug}' not found")
    return _strip_mongo_id(doc)


@api.get("/info-pages")
async def list_info_pages():
    await _ensure_seeded()
    docs = await db.info_pages.find().to_list(100)
    return [_strip_mongo_id(d) for d in docs]


@api.get("/info-pages/{slug}")
async def get_info_page(slug: str):
    await _ensure_seeded()
    doc = await db.info_pages.find_one({"slug": slug})
    if not doc:
        raise HTTPException(404, f"Info page '{slug}' not found")
    return _strip_mongo_id(doc)


# ---------- Search (rate-limited) ----------
@api.get("/search")
@limiter.limit("60/minute")
async def search(
    request: Request,
    q: str = Query("", description="Search query", max_length=100),
    scope: str = Query("Entire Catalog", description="Entire Catalog | Programs | Courses"),
):
    await _ensure_seeded()
    if scope not in ("Entire Catalog", "Programs", "Courses"):
        raise HTTPException(400, "Invalid scope")

    q_stripped = q.strip()
    if not q_stripped:
        return {"query": q, "scope": scope, "results": []}

    needle = q_stripped.lower()
    results: List[dict] = []

    if scope in ("Entire Catalog", "Programs"):
        nav_doc = await db.nav.find_one({"_id": "nav-tree"})
        tree = nav_doc.get("tree", []) if nav_doc else []
        for n in tree:
            if needle in n["label"].lower():
                results.append(
                    {
                        "label": n["label"],
                        "url": f"/en/2024-25/catalog/{n['slug']}",
                        "type": "Section",
                    }
                )
            for child in n.get("children", []) or []:
                if needle in child["label"].lower():
                    results.append(
                        {
                            "label": f"{n['label']} \u203a {child['label']}",
                            "url": f"/en/2024-25/catalog/{n['slug']}/{child['slug']}",
                            "type": "Page",
                        }
                    )

    if scope in ("Entire Catalog", "Courses"):
        depts = await db.departments.find().to_list(100)
        for d in depts:
            for c in d.get("courses", []):
                if (
                    needle in c.get("code", "").lower()
                    or needle in c.get("title", "").lower()
                    or needle in c.get("desc", "").lower()
                ):
                    results.append(
                        {
                            "label": f"{c['code']} \u2013 {c['title']}",
                            "url": f"/en/2024-25/catalog/courses-credits-hours/{d['slug']}",
                            "type": "Course",
                        }
                    )

    return {"query": q_stripped, "scope": scope, "count": len(results), "results": results}


# ---------- Status (kept for backward compatibility) ----------
class StatusCheck(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str = Field(..., min_length=1, max_length=200)


class StatusCheckCreate(BaseModel):
    client_name: str = Field(..., min_length=1, max_length=200)


@api.post("/status", response_model=StatusCheck)
@limiter.limit("30/minute")
async def create_status_check(request: Request, input: StatusCheckCreate):
    obj = StatusCheck(client_name=input.client_name)
    await db.status_checks.insert_one(obj.dict())
    return obj


@api.get("/status", response_model=List[StatusCheck])
async def get_status_checks():
    items = await db.status_checks.find().to_list(1000)
    return [StatusCheck(**i) for i in items]


# ---------- App wiring ----------
app.include_router(api)

# Security headers FIRST so it wraps everything.
app.add_middleware(SecurityHeadersMiddleware)

# CORS: explicit allowlist via env; default to wildcard READ-ONLY (no credentials).
cors_origins_env = os.environ.get("CORS_ORIGINS", "*").strip()
if cors_origins_env == "*":
    allow_origins = ["*"]
else:
    allow_origins = [o.strip() for o in cors_origins_env.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=False,  # no cookies/sessions; safer with wildcards
    allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "X-Admin-Key"],
    max_age=600,
)


@app.on_event("startup")
async def startup_seed():
    try:
        await _ensure_seeded()
        logger.info("Startup seed check completed")
    except Exception as e:  # pragma: no cover
        logger.exception("Startup seed failed: %s", e)


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
