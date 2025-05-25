from __future__ import annotations

from pydantic import BaseModel


class DomainModel(BaseModel):
    model_config = {
        "frozen": True,
    }
