from datetime import date

from sqlalchemy import select, and_, or_, func

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker, engine
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.hotels.schemas import SGetHotelsResponse


class HotelDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def find_all_available(cls, location: str, date_from: date, date_to: date) -> [SGetHotelsResponse]:
        async with (async_session_maker() as session):
            avlbl_rooms = select(
                Hotels.id, Hotels.name, Hotels.location, Hotels.services, Hotels.rooms_quantity, Hotels.image_id,
                (Rooms.quantity - func.count(Bookings.room_id)).label('rooms_left')).select_from(Hotels).join(
                Rooms, Rooms.hotel_id == Hotels.id).join(Bookings, Bookings.room_id == Rooms.id, isouter=True).where(
                and_(Hotels.location.like(f'%{location}%'),
                     or_(
                         and_(Bookings.date_from >= date_from, Bookings.date_from <= date_to),
                         and_(Bookings.date_from <= date_from, Bookings.date_to > date_from),
                         Bookings.date_from.is_(None)
                     ))).group_by(
                Hotels.id, Rooms.quantity).having(Rooms.quantity - func.count(Bookings.room_id) > 0).cte(
                'available_hotel_rooms')

            query = select(avlbl_rooms).select_from(avlbl_rooms)
            print(avlbl_rooms.compile(engine, compile_kwargs={"literal_binds": True}))
            result = await session.execute(query)
            result_list = result.fetchall()
            print(result_list)

            return result_list
