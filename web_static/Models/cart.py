from sqlalchemy import Column, Integer, ForeignKey
from baseModels import BaseModel, Base

class Cart(BaseModel, Base):
    """Cart class created"""
    __tablename__ = 'cart'
    product_id = Column(Integer, ForeignKey('products.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    quantity = Column(Integer, nullable=False)