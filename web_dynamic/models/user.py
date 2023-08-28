from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.baseModels import BaseModel, Base

class User(BaseModel, Base):
    """creating user table"""
    __tablename__ = "users"
    username = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(20), nullable=False)
    phone_number = Column(Integer, nullable=False)
    billing_addr = relationship('BillingAddress', back_populates='user', cascade="all, delete-orphan")
    ratings = relationship('Rating', back_populates='order_Items', cascade='all, delete-orphan')
    comments = relationship('Comment', back_populates='users', cascade="all, delete-orphan")
    transactions = relationship('Transaction', back_populates='users', cascade='all, delete-orphan')
    carts = relationship('Cart', back_populates='users', cascade="all, delete-orphan")
