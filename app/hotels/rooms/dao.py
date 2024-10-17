from datetime import date

from sqlalchemy import select, func, and_

from app.database import async_session_maker, engine
from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms


class RoomDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def find_all(cls, hotel_id: int, date_from: date, date_to: date):
        query = select(Rooms.id, Rooms.hotel_id, Rooms.name, Rooms.description, Rooms.price, Rooms.services,
                       Rooms.quantity,
                       Rooms.image_id, ((func.date_part('day', date_to) -
                                         func.date_part('day', date_from)) * Rooms.price).label('total_cost'),
                       (Rooms.quantity - func.count(Bookings.date_to)).label('rooms_left')
                ).select_from(Hotels
                ).join(Rooms, and_(Rooms.hotel_id == Hotels.id, Hotels.id == hotel_id)
                ).join(Bookings,
                       and_((Bookings.room_id == Rooms.id),
                            and_(Bookings.date_from < date_to, Bookings.date_to > date_from),
                            ), isouter=True
                ).group_by(Rooms.id)

        async with async_session_maker() as session:
            print(query.compile(engine, compile_kwargs={"literal_binds": True}))
            result = await session.execute(query)
            result_list = result.fetchall()
            result_list = result_list if result_list else []
            print(result_list)
            return result_list
