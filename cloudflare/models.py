from __future__ import annotations

from pydantic import BaseModel


class GetZonesResponse(BaseModel):
    success: bool
    result: list[ZoneEntity]


class ZoneEntity(BaseModel):
    id: str
    name: str
