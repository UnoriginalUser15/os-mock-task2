from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from ..database import Base


class HotelBooking(Base):
    __tablename__ = "hotel_booking"

    hotel_ID = Column(Integer, primary_key=True, index=True)
    user_ID = Column(Integer, ForeignKey("user_table.user_ID"))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    room_ID = Column(Integer, ForeignKey("room_table.room_ID"))

    # links the table to other tables
    user = relationship("UserTable", back_populates="hotel")
    room = relationship("RoomTable", back_populates="hotel")
