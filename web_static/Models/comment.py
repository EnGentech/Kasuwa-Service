from sqlalchemy import Column, String, ForeignKey, Integer
from baseModels import BaseModel, Base

class Comment(BaseModel, Base):
    """Comment class built"""
    __tablename__ = 'comments'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    message = Column(String(200))
