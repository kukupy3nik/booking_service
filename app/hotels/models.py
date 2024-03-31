from sqlalchemy import Column, Integer, String, JSON, ForeignKey

from app.database import Base


class Hotel(Base):
    __tablename__ = 'hotel'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)


class Room(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey('hotel.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=False)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)