from fastapi import FastAPI, APIRouter, HTTPException, Query
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
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

app = FastAPI(title="IIT Jammu SmartCatalog API")
api = APIRouter(prefix="/api")

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


# ---------- Models ----------
class Course(BaseModel):
    code: str
    title: str
    credits: int
    hours: str
    desc: str


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


class CalendarRow(BaseModel):
    event: str
    date: str


class CalendarTerm(BaseModel):
    term: str
    rows: List[CalendarRow]


class FeeTable(BaseModel):
    heading: str
    columns: List[str]
    rows: List[List[str]]


class FeeSection(BaseModel):
    slug: str
    title: str
    intro: str
    tables: List[FeeTable]


class InfoPage(BaseModel):
    slug: str
    title: str
    body: List[str]


class NavItem(BaseModel):
    slug: str
    label: str
    children: Optional[List[Any]] = None


class SearchResult(BaseModel):
    label: str
    url: str
    type: str


# ---------- Helpers ----------
def _strip_mongo_id(doc: dict) -> dict:
    doc.pop("_id", None)
    return doc


# ---------- Seed ----------
@api.post("/seed")
async def seed_database(force: bool = False):
    """Seed the DB with initial IIT Jammu catalog content. Safe to call multiple times.

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

    # Departments
    for dept in DEPARTMENTS:
        await db.departments.update_one(
            {"slug": dept["slug"]}, {"$set": dept}, upsert=True
        )
    # Faculty groups
    for fg in FACULTY_GROUPS:
        await db.faculty_groups.update_one(
            {"slug": fg["slug"]}, {"$set": fg}, upsert=True
        )
    # Calendar terms
    for term in ACADEMIC_CALENDAR:
        await db.calendar.update_one(
            {"term": term["term"]}, {"$set": term}, upsert=True
        )
    # Fees
    for fee in FEES_DATA:
        await db.fees.update_one({"slug": fee["slug"]}, {"$set": fee}, upsert=True)
    # Info pages
    for info in INFO_PAGES:
        await db.info_pages.update_one(
            {"slug": info["slug"]}, {"$set": info}, upsert=True
        )
    # Nav
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
    if await db.departments.count_documents({}) == 0:
        await seed_database(False)


# ---------- Routes ----------
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


class CourseCreate(BaseModel):
    code: str
    title: str
    credits: int
    hours: str
    desc: str


@api.post("/departments/{slug}/courses")
async def add_course(slug: str, course: CourseCreate):
    await _ensure_seeded()
    dept = await db.departments.find_one({"slug": slug})
    if not dept:
        raise HTTPException(404, f"Department '{slug}' not found")
    # Reject duplicate code
    if any(c.get("code") == course.code for c in dept.get("courses", [])):
        raise HTTPException(409, f"Course '{course.code}' already exists in {slug}")
    await db.departments.update_one(
        {"slug": slug}, {"$push": {"courses": course.dict()}}
    )
    return {"status": "ok", "added": course.code}


@api.delete("/departments/{slug}/courses/{code}")
async def remove_course(slug: str, code: str):
    res = await db.departments.update_one(
        {"slug": slug}, {"$pull": {"courses": {"code": code}}}
    )
    if res.modified_count == 0:
        raise HTTPException(404, "Course not found")
    return {"status": "ok", "removed": code}


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


# ---------- Search ----------
@api.get("/search")
async def search(
    q: str = Query("", description="Search query"),
    scope: str = Query("Entire Catalog", description="Entire Catalog | Programs | Courses"),
):
    await _ensure_seeded()
    if not q.strip():
        return {"query": q, "scope": scope, "results": []}

    needle = q.lower()
    results: List[dict] = []

    # Programs / sections from nav tree
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

    # Courses
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

    return {"query": q, "scope": scope, "count": len(results), "results": results}


# ---------- Status (kept for backward compatibility) ----------
class StatusCheck(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str


class StatusCheckCreate(BaseModel):
    client_name: str


@api.post("/status", response_model=StatusCheck)
async def create_status_check(input: StatusCheckCreate):
    obj = StatusCheck(client_name=input.client_name)
    await db.status_checks.insert_one(obj.dict())
    return obj


@api.get("/status", response_model=List[StatusCheck])
async def get_status_checks():
    items = await db.status_checks.find().to_list(1000)
    return [StatusCheck(**i) for i in items]


app.include_router(api)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_seed():
    try:
        await _ensure_seeded()
        logger.info("Seed check completed")
    except Exception as e:  # pragma: no cover
        logger.exception("Seed failed: %s", e)


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
