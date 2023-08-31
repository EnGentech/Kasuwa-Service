from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.baseModels import BaseModel, Base

class Category(BaseModel, Base):
    """category page created"""
    __tablename__ = 'categories'
    category = Column(String(15), nullable=False)
    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")
