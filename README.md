# IIT Jammu SmartCatalog — Local Setup

This is the IIT Jammu academic-catalog clone built on Emergent.

- **Frontend:** React 19 + react-router 7 + Tailwind + craco (CRA) — runs on port **3000**
- **Backend:** FastAPI + Motor (async MongoDB) + Pydantic — runs on port **8001**
- **Database:** MongoDB 7 — runs on port **27017**

## 1. Download / get the code from Emergent

On the Emergent workspace, **Save to GitHub** is the primary export path:

1. Click your profile icon at the top, then **Connect GitHub** (one-time) and authorise Emergent.
2. In the chat panel, click **Save to GitHub**.
3. Choose / create a branch and click **PUSH TO GITHUB**.
4. Clone the new repo locally:

   ```bash
   git clone https://github.com/<you>/<repo>.git
   cd <repo>
   ```

> Note: `.env` files and secrets are **not** pushed for security. You will set them up locally below.
>
> A direct "Download ZIP" is not available; the GitHub flow is the official way.

## 2. One-command local startup (recommended)

Prerequisites: Docker + Docker Compose.

```bash
cp backend/.env.example backend/.env   # optional, defaults already work for Docker
docker compose up --build
```

This starts three containers:

| Service  | URL                       |
| -------- | ------------------------- |
| Frontend | http://localhost:3000     |
| Backend  | http://localhost:8001/api |
| Mongo    | mongodb://localhost:27017 |

The backend auto-seeds the database on first request. To force a reseed:

```bash
curl -X POST "http://localhost:8001/api/seed?force=true"
```

Stop: `docker compose down`. Wipe Mongo volume too: `docker compose down -v`.

## 3. Manual local setup (without Docker)

### MongoDB

Either install MongoDB 7+ natively or run it in a single container:

```bash
docker run -d --name iitj-mongo -p 27017:27017 -v iitj-mongo-data:/data/db mongo:7
```

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create `backend/.env`:

```
MONGO_URL=mongodb://localhost:27017
DB_NAME=iitjammu_catalog
```

Run:

```bash
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

Health check: `curl http://localhost:8001/api/`

### Frontend

```bash
cd frontend
yarn install
```

Create `frontend/.env`:

```
REACT_APP_BACKEND_URL=http://localhost:8001
```

Run:

```bash
yarn start
```

Open <http://localhost:3000> — the app redirects to `/en/2024-25/catalog`.

## 4. Catalog content

All catalog data (12 departments, 12 faculty groups, fees, calendar, info pages, navigation tree, catalog versions) lives in **`backend/seed_data.py`**. Edit there and re-seed:

```bash
curl -X POST "http://localhost:8001/api/seed?force=true"
```

The frontend has a fallback mock in `frontend/src/data/mock.js` (used when the API is unreachable) — keep it in sync if you change the navigation tree.

## 5. Key API endpoints

| Method | Path                                       | Description                          |
| ------ | ------------------------------------------ | ------------------------------------ |
| GET    | `/api/`                                    | Health check                         |
| GET    | `/api/meta`                                | Catalog versions + current           |
| GET    | `/api/nav`                                 | Sidebar navigation tree              |
| GET    | `/api/departments`                         | All 12 departments                   |
| GET    | `/api/departments/{slug}`                  | Department with course list          |
| POST   | `/api/departments/{slug}/courses`          | Add a course                         |
| DELETE | `/api/departments/{slug}/courses/{code}`   | Remove a course                      |
| GET    | `/api/faculty`                             | All 12 faculty groups                |
| GET    | `/api/faculty/{slug}`                      | Faculty group with members           |
| GET    | `/api/calendar`                            | Academic calendar terms              |
| GET    | `/api/fees`                                | All 7 fee sections                   |
| GET    | `/api/fees/{slug}`                         | One fee section with tables          |
| GET    | `/api/info-pages`                          | All info / policy / program pages    |
| GET    | `/api/info-pages/{slug}`                   | One info page                        |
| GET    | `/api/search?q=...&scope=...`              | Search; scope = Entire Catalog \| Programs \| Courses |
| POST   | `/api/seed[?force=true]`                   | Seed / reseed MongoDB                |

## 6. Production builds

Frontend production build:

```bash
cd frontend
yarn build
# serve build/ with nginx, vercel, netlify, etc.
```

Backend production (gunicorn with uvicorn workers):

```bash
cd backend
pip install "uvicorn[standard]" gunicorn
gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8001 server:app
```

Remember to set `REACT_APP_BACKEND_URL` to your production backend URL at build time.
