from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    first_name =  Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    
    trips = relationship("Trip", back_populates="user", cascade="all, delete")


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    destination_city = Column(String, index=True)
    start_date = Column(Date)
    end_date = Column(Date)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="trips")