from sqlalchemy import Column, Integer, String, JSON, ForeignKey

from app.database import Base


class Rooms(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey('hotel.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=False)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)