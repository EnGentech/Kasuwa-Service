from sqlalchemy import Column, String
from sql_connection import Base
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """creating base models for other clases"""
    id = Column(String(125), default=uuid4, nullable=False, primary_key=True)
    date_created = Column(String(60), nullable=False, default=datetime.utcnow())