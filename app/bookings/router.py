from fastapi import APIRouter

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get('')
async def get_bookings() -> list[SBooking]:
    return await BookingDAO.find_all()


@router.get('/{id}')
async def get_booking(id: int):
    return await BookingDAO.find_by_id(id)



# @router.get('/{booking_id}')
# def get_booking(booking_id: int):
#     pass