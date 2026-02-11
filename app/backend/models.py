from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy import Column, String, Float, Integer, DateTime, Boolean, ForeignKey
from datetime import datetime


class Base(DeclarativeBase):
    pass


class UserTable(Base):
    __tablename__ = "user_table"

    user_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(length=64), nullable=False)
    email = Column(String(length=64), nullable=False)
    password = Column(String(length=64), nullable=False)
    is_admin = Column(Boolean, default=False)
    loyalty_points = Column(Integer, default=0)

    # links the table to other tables
    hotel = relationship("HotelBooking", back_populates="user")
    zoo = relationship("ZooBooking", back_populates="user")


class HotelBooking(Base):
    __tablename__ = "hotel_booking"

    hotel_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_ID = Column(Integer, ForeignKey("user_table.user_ID"))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    room_ID = Column(Integer, ForeignKey("room_table.room_ID"))

    # links the table to other tables
    user = relationship("UserTable", back_populates="hotel")
    room = relationship("RoomTable", back_populates="hotel")


class ZooBooking(Base):
    __tablename__ = "zoo_booking"

    visit_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    child_tickets = Column(Integer, nullable=False)
    adult_tickets = Column(Integer, nullable=False)
    educational_visit = Column(Boolean, nullable=False, default=False)
    user_ID = Column(Integer, ForeignKey("user_table.user_ID"))

    user = relationship("UserTable", back_populates="zoo")


class RoomTable(Base):
    __tablename__ = "room_table"
    
    room_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    is_booked = Column(Boolean, default=False)
    room_type = Column(String(length=64), nullable=False)
    latest_booking = Column(DateTime, nullable=False, default=datetime.now())
    room_price = Column(Float, nullable=False)

    # links the table to other table
    hotel = relationship("HotelBooking", back_populates="room")
