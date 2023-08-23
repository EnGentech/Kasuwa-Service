from sqlalchemy import Column, String, Integer, ForeignKey
from baseModels import BaseModel, Base
from user import User

class Rating(BaseModel, Base):
    """A class definition to define rating table"""
    __tablename__ = 'ratings'
    User_id = Column(Integer, ForeignKey(User.id))
    