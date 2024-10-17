from datetime import date

from app.hotels.rooms.schemas import SGetRoomsResponse
from app.hotels.router import router
from app.hotels.rooms.dao import RoomDAO


@router.get('/{hotel_id}/rooms')
async def get_rooms(hotel_id: str, date_from: date, date_to: date):  # -> list[SGetRoomsResponse]:
    try:
        rooms = await RoomDAO.find_all(int(hotel_id), date_from, date_to)
    except Exception as e:
        return str(e)

    return [SGetRoomsResponse(id=room[0],
                              hotel_id=room[1],
                              name=room[2],
                              description=room[3],
                              price=room[4],
                              services=room[5],
                              quantity=room[6],
                              image_id=room[7],
                              total_cost=room[8],
                              rooms_left=room[9])
            for room in rooms]


