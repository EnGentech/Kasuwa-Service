from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from base import Base, BaseModel




class OrderItem(BaseModel, Base):
    __tablename__ = 'order_items'

    quantity = Column(Integer, nullable=False)
    Price_per_item = Column(Float, nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='order_item')
    order = relationship('Order', back_populates='order_item', cascade='all, delete-orphan')