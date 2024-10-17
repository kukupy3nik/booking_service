from pydantic import BaseModel


class SRoom(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    price: int
    services: list[str]
    quantity: int
    image_id: int


class SGetRoomsResponse(SRoom):
    total_cost: int
    rooms_left: int

