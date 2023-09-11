from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models.baseModels import BaseModel, Base

class BillingAddress(BaseModel, Base):
    """created class for Billing Address"""
    __tablename__ = 'billing_address'
    nationality = Column(String(100), nullable=False)
    contact_name = Column(String(155), nullable=False)
    mobile_number = Column(String(20), nullable=False)
    address = Column(String(200), nullable=False)
    state = Column(String(100), nullable=False)
    lga = Column(String(200), nullable=False)
    zip_code = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='billing_addr')