from __future__ import annotations

from pydantic import BaseModel


class Response(BaseModel):
    disclaimer: str
    license: str
    timestamp: int
    base: str
    rates: dict[str, float]
