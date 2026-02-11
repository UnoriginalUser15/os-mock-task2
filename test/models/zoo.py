from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey
from ..database import Base


class ZooBooking(Base):
    __tablename__ = "zoo_booking"

    visit_ID = Column(Integer, primary_key=True, index=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    child_tickets = Column(Integer, nullable=False)
    adult_tickets = Column(Integer, nullable=False)
    educational_visit = Column(Boolean, nullable=False, default=False)
    user_ID = Column(Integer, ForeignKey("user_table.user_ID"))

    user = relationship("UserTable", back_populates="zoo")
