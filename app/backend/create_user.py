from sqlalchemy.orm import Session
from database import engine
from models import UserTable
import hashlib
from passlib.hash import argon2


# creates a new account in 'user_table' in data.db
def create_account(username, email, password):
    password = input("password:")
    print(password)
    password = password.encode("utf-8")
    hashed_pass = hashlib.sha256(password)
    print(hashed_pass)
    
    # with Session(engine) as session:
    #     session.add(username=username, email=email, password=hashed_pass)
    #     session.commit()

create_account("user", "email", "password")