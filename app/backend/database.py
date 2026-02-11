import sqlalchemy
import os
from models import Base, HotelBooking, RoomTable, UserTable, ZooBooking


# this makes sqlalchemy actually make the database, don't ask
__all__ = [
    "HotelBooking",
    "ZooBooking",
    "RoomTable",
    "UserTable"
]

# gets the absolute directory of backend
path = os.path.dirname(__file__)
path = "sqlite:///"+path+"/data/data.db"

engine = sqlalchemy.create_engine(path, echo=True)

# creates all tables in the database
Base.metadata.create_all(engine)
