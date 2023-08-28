from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.baseModels import Base, BaseModel

class Cart(BaseModel, Base):
    """Cart class created"""
    __tablename__ = 'carts'
    product_id = Column(Integer, ForeignKey('products.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    quantity = Column(Integer, nullable=False)
    users = relationship('User', back_populates='carts')
    products = relationship('Products', back_populates='carts', cascade='all, delete-orphan')
    