from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer,Float, Boolean, String, DateTime
from ..database import Base


class RoomTable(Base):
    __tablename__ = "room_table"
    
    room_ID = Column(Integer, primary_key=True)
    is_booked = Column(Boolean, default=False)
    room_type = Column(String, nullable=False)
    latest_booking = Column(DateTime, nullable=False)
    room_price = Column(Float, nullable=False)

    # links the table to other table
    hotel = relationship("HotelBooking", back_populates="room")