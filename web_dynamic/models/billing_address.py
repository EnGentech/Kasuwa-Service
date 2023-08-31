from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.baseModels import BaseModel, Base

class BillingAddress(BaseModel, Base):
    """created class for Billing Address"""
    __tablename__ = 'billing_address'
    billing_address = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='billing_addr')