from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from base import Base, BaseModel


class BillingAddress(BaseModel, Base):
    __tablename__ = 'billing_address'

    phoneNumber = Column(String(50), nullable=False)
    billing_address = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='bill_address')
