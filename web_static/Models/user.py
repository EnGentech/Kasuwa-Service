from sqlalchemy import Column, String, Integer
from models.baseModels import BaseModel, Base

class User(BaseModel, Base):
    """creating user table"""
    __tablename__ = "users"
    username = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(20), nullable=False)
    phone_number = Column(Integer, nullable=False)