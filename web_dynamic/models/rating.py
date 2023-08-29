from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.baseModels import BaseModel, Base

class Rating(BaseModel, Base):
    """A class definition to define rating table"""
    __tablename__ = 'ratings'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    rating = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    products = relationship('Product', back_populates='ratings')
    users = relationship('User', back_populates='ratings')