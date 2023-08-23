from sqlalchemy import Column, String
from sql_connection import Base
from uuid import uuid4
from datetime import datetime

class User(Base):
    """creating user table"""
    __tablename__ = "users"
    id = Column(String(125), default=uuid4, nullable=False)
    username = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    date_created = Column(String(60), nullable=False, default=datetime.utcnow())