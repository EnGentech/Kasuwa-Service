from sqlalchemy import Column, String
from models.baseModels import BaseModel, Base

class Caterory(BaseModel, Base):
    """category page created"""
    __tablename__ = 'categories'
    category = Column(String(15), nullable=False)
