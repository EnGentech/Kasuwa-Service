from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.baseModels import BaseModel, Base

class Comment(BaseModel, Base):
    """Comment class built"""
    __tablename__ = 'comments'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    message = Column(String(200))
    users = relationship('User', back_populates='comments')
    products = relationship('Product', back_populates='comments')