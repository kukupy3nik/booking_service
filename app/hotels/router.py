from datetime import date

from fastapi import APIRouter

from app.hotels.rooms.schemas import SGetRoomsResponse
from app.hotels.schemas import SGetHotelsResponse, SHotel
from app.hotels.dao import HotelDAO

router = APIRouter(prefix="/hotels", tags=["Отели"])


@router.get('/{location}')
async def get_hotels(location: str, date_from: date, date_to: date):  # -> list[SGetHotelsResponse]:
    hotels = await HotelDAO.find_all_available(location=location, date_from=date_from, date_to=date_to)
    return [SGetHotelsResponse(
        id=h[0], name=h[1], location=h[2], services=h[3], rooms_quantity=h[4], image_id=h[5], rooms_left=h[6])
        for h in hotels]


@router.get('/{hotel_id}/rooms')
def get_rooms(hotel_id: str, date_from: date, date_to: date) -> list[SGetRoomsResponse]:
    ...



@router.get('/{hotel_id}')
def get_hotel(hotel_id: int) -> SHotel:
    pass

