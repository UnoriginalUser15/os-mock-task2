import sqlalchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine
import sqlite3
import os
from models import Base, HotelBooking, RoomTable, UserTable, ZooBooking


# this makes sqlalchemy actually make the database, don't ask
__all__ = [
    "HotelBooking",
    "ZooBooking",
    "RoomTable",
    "UserTable"
]

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

# gets the absolute directory of backend
path = os.path.dirname(__file__)
path = "sqlite:///"+path+"/data/data.db"

engine = sqlalchemy.create_engine(path, echo=True)

# creates all tables in the database
Base.metadata.create_all(engine)
