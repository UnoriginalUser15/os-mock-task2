from sqlalchemy.orm import Session
from database import engine
from models import RoomTable


# used to create new rooms in 'room_table' in data.db
def create_room(room_type, room_price, num_of_rooms):
    #### ALL OF THE INPUT IS TEMP FOR TESTING
    # list of room types
    room_list = ["single", "twin", "double"]
    # indexes to room type
    room_type = room_list[int(input("room type (1=single, 2=twin, 3=double): ")) - 1]
    # gets price of room
    room_price = round(float(input("room price: ")), 2)
    # gets number of that room
    num_of_rooms = int(input("num of rooms: "))

    # creates session to add the desired room(s)
    with Session(engine) as session:
        for i in range(num_of_rooms):
            session.add(RoomTable(room_type=room_type, room_price=room_price))

        session.commit()

# temp running of the function for testing
create_room("","","")