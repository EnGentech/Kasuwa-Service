from sqlalchemy import Column, String, Integer, Enum, Date
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from base import Base, BaseModel
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    __tablename__ = 'users'

    username = Column(String(length=50), nullable=False, unique=True)
    fullname = Column(String(length=50), nullable=False, unique=False)
    email = Column(String(length=50), nullable=False, unique=True)
    address = Column(String(length=200))
    phone = Column(String(length=20))
    GENDER_CHOICES = ['male', 'famale']
    gender = Column(Enum(*GENDER_CHOICES, name='gender_enum'))
    birthDate = Column(Date)
    created_at = Column(String(length=60), nullable=False, default=datetime.utcnow())
    updated_at = Column(String(length=60), nullable=True, default=datetime.utcnow())
    carts = relationship('Cart', back_populates='user', single_parent=True)
    transaction = relationship('Transaction', back_populates='user', cascade='all, delete-orphan')
    ratings = relationship('Rating', back_populates='user', cascade="all, delete-orphan")
    bill_address = relationship('BillingAddress', back_populates='user', cascade="all, delete-orphan")
    comments = relationship('Comments', back_populates='user', cascade='all, delete-orphan')
    order = relationship('Order', back_populates='user', cascade='all, delete-orphan')
    order_item = relationship('OrderItem', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f'Username: {username}'