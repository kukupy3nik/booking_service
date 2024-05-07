from datetime import date
from typing import Optional

from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel, Field

from app.bookings.router import router as router_bookings


app = FastAPI()
app.include_router(router_bookings)


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


class SHotel(BaseModel):
    address: str
    name: str
    stars: int = Field(None, ge=1, le=5)


@app.get("/hotels")
def get_hotels(search_args: HotelsSearchArgs = Depends()) -> list[SHotel]:
    return [SHotel(address='Aa st.', name='Hotel C', stars=5), SHotel(address='Bb st.', name='Hotel D', stars=5)]




if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app.main:app', host="127.0.0.1", port=8000, reload=True)