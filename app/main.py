from datetime import date
from typing import Optional

from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel, Field

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels


app = FastAPI()
app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app.main:app', host="127.0.0.1", port=8000, reload=True)