from datetime import date

from sqlalchemy import select, and_, or_, func
from sqlalchemy.sql.selectable import Select

from app.database import async_session_maker, engine
from app.bookings.models import Bookings
from app.hotels.models import Rooms
from app.users.models import Users
from app.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(cls, user_id: int, room_id: int, date_from: date, date_to: date):
        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                and_(Bookings.room_id == room_id,
                     or_(
                         and_(Bookings.date_from >= date_from, Bookings.date_from <= date_to),
                         and_(Bookings.date_from <= date_from, Bookings.date_to > date_from)
                     ))).cte('booked_rooms')

            get_rooms_left: Select = select(
                Rooms.quantity - func.count(booked_rooms.c.id)
            ).select_from(Rooms).join(
                booked_rooms, Rooms.id == booked_rooms.c.room_id, isouter=True
            ).where(Rooms.id == room_id).group_by(Rooms.id)

            print(get_rooms_left.compile(engine, compile_kwargs={"literal_binds": True}))

            rooms_left = await session.execute(get_rooms_left)
            rooms_left = rooms_left.scalar()
            print(rooms_left)
            if rooms_left >= 1:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price: int = price.scalar()
                model = await super().add(user_id=user_id, room_id=room_id, date_from=date_from, date_to=date_to, price=price)
                return model.scalar()
            else:
                return None
