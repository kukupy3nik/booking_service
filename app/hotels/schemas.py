from datetime import date
from typing import Optional

from pydantic import BaseModel
from fastapi import Query


class SHotel(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int


class SGetHotelsResponse(SHotel):
    rooms_left: int


class HotelsSearchArgs:
    def __init__(self,
                 location: str,
                 date_from: date,
                 date_to: date,
                 has_spa: Optional[bool] = None,
                 stars: int | None = Query(None, ge=1, le=5),):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars