from sqlalchemy import Column, String, Integer
from datetime import datetime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BaseModel():
    """creating base models for other clases"""
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    date_created = Column(String(60), nullable=False, default=datetime.utcnow())