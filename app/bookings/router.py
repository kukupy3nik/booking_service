from fastapi import APIRouter, Depends

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.users.models import Users
from app.users.dependencies import get_current_user, get_current_user

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)
    # return await BookingDAO.find_all()


# @router.get('/{id}')
# async def get_booking(id: int):
#     return await BookingDAO.find_by_id(id)



# @router.get('/{booking_id}')
# def get_booking(booking_id: int):
#     pass