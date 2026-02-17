from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import List

# -------- USERS --------

#Base Schema other classes will inherit instead repeating common fields
class UserBase(BaseModel):
    """ Base User Schema"""
    name: str
    email: str

class UserCreate(UserBase):
    """User Creation Schema"""
    password: str

class UserResponse(UserBase):
    """User Response Schema"""

    #Server Returns the id from the database
    id: int

    #Allows pydantic to readd data from ORM objects like SQLAlchemy models, not just dictionaries "from_attriburtes = True"
    model_config = ConfigDict(from_attributes=True)


# -------- TRIPS --------

class TripBase(BaseModel):
    destination_city: str
    start_date: date
    end_date: date

class TripCreate(TripBase):
    user_id: int

class TripResponse(TripBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True