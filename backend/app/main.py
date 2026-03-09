from datetime import datetime, timezone
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MediaMinds VCR API", version="0.1.0")


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str
    timestamp_utc: str


class ClientCreateRequest(BaseModel):
    name: str
    industry: str | None = None
    website: str | None = None


@app.get("/api/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service="vcr-backend",
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
    )


@app.get("/api/clients")
def list_clients() -> dict:
    return {"items": [], "total": 0}


@app.post("/api/clients")
def create_client(payload: ClientCreateRequest) -> dict:
    return {
        "id": "placeholder-client-id",
        "name": payload.name,
        "industry": payload.industry,
        "website": payload.website,
        "created": True,
    }


@app.get("/api/clients/{uuid}/vcr")
def get_vcr(uuid: str) -> dict:
    return {
        "client_uuid": uuid,
        "tier_distribution": {"A": 0, "B": 0, "C": 0, "D": 0},
        "velocity_score": 0,
        "content_opportunities": 0,
    }
