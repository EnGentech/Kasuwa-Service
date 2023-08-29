from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from base import Base, BaseModel



class Cart(BaseModel, Base):
    __tablename__ = 'cart'


    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='carts')
    items_id = Column(Integer, ForeignKey('cart_items.id'))
    items = relationship('CartItems', back_populates='cart')