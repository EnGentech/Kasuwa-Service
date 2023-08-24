from sqlalchemy import Column, String, Integer
from connector.sql_connection import Base
from datetime import datetime

class BaseModel:
    """creating base models for other clases"""
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    date_created = Column(String(60), nullable=False, default=datetime.utcnow())