from sqlalchemy import Column, Integer, String, JSON, Date, ForeignKey, Computed

from app.database import Base


class Booking(Base):
    __tablename__ = 'booking'
    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey('room.id'))
    user_id = Column(ForeignKey('user.id'))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed('price * (date_from - date_to)'))
    total_days = Column(Integer, Computed('(date_from - date_to)'))