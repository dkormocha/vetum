from pydantic import BaseModel
from datetime import date
from typing import List

# -------- USERS --------

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


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