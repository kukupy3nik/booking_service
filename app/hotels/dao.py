from datetime import date

from sqlalchemy import select, and_, func, case

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
            booked_rooms = select(Bookings.room_id, (Rooms.quantity - func.count(Bookings.room_id)).label(
                'rooms_left')).select_from(Bookings).join(Rooms, Rooms.id == Bookings.room_id).where(
                and_(Bookings.date_from < date_to, Bookings.date_to > date_from)).group_by(
                Bookings.room_id, Rooms.quantity).cte('booked_rooms')

            avlbl_rooms = select(
                Hotels.id,
                Hotels.name,
                Hotels.location,
                Hotels.services,
                func.sum(Rooms.quantity).label('rooms_quantity'),
                Hotels.image_id, func.sum(case((
                    booked_rooms.c.rooms_left == None, Rooms.quantity), else_=booked_rooms.c.rooms_left)).label('rooms_left')
            ).select_from(Hotels
                  ).join(Rooms, Rooms.hotel_id == Hotels.id
                         ).join(booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True
            ).where(Hotels.location.like(f'%{location}%')
            ).group_by(Hotels.id
            ).having(func.sum(case((
                    booked_rooms.c.rooms_left == None, Rooms.quantity), else_=booked_rooms.c.rooms_left)) > 0)

            result = await session.execute(avlbl_rooms)
            return result.fetchall()
