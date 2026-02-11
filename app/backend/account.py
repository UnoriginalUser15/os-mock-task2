from sqlalchemy.orm import Session
from database import engine
from models import UserTable
from passlib.hash import argon2


# creates a new account in 'user_table' in data.db
def create_account(username, email, password):
    #### ALL OF THE INPUT IS TEMP FOR TESTING
    username = input("username: ")

    email = input("email: ")
    
    admin = bool(input("admin: "))

    points = int(input("loyalty points: "))

    password = input("password: ")
    
    # hashes the password
    hashed_pass = argon2.hash(password)

    with Session(engine) as session:
        # adds the user to the database
        session.add(UserTable(username=username, email=email, password=hashed_pass, is_admin=admin, loyalty_points=points))
        session.commit()
    
    # verifies is the password is correct and returns a bool
    print(argon2.verify(password, hashed_pass))

create_account("user", "email", "password")