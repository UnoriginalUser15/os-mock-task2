from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean
from ..database import Base


class UserTable(Base):
    __tablename__ = "user_table"

    user_ID = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    loyalty_points = Column(Integer, default=0)

    # links the table to other tables
    hotel = relationship("HotelBooking", back_populates="user")
    zoo = relationship("ZooBooking", back_populates="user")
