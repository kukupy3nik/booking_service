from app.dao.base import BaseDAO
from app.hotels.rooms.models import Rooms


class HotelDAO(BaseDAO):
    model = Rooms
