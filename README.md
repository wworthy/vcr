# MediaMinds VCR (Velocity Competitive Radar)

AI-driven competitive intelligence platform for SEO, social velocity tracking, and content strategy generation.

## What this repo now includes

- A **working backend scaffold** (FastAPI) with foundational API routes.
- A **project docs set** split into product and architecture references.
- A **deployment-oriented directory layout** aligned to `/opt/vcr/*`.

## Repository layout

- `backend/` — FastAPI service and Python dependencies
- `frontend/` — Angular app placeholder
- `workers/` — background worker placeholder
- `scripts/` — automation script placeholder
- `logs/` — local log output directory
- `docs/` — product + architecture reference docs

## Quick start (backend)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload --port 8000
```

Then open `http://localhost:8000/api/health`.

## Documentation

- Product blueprint: `docs/product-spec.md`
- System architecture: `docs/architecture.md`
