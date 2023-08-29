# from associations import transactions_products_association
from sqlalchemy import Column, String, Integer, Enum, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from base import Base, BaseModel



class Transaction(BaseModel, Base):
    __tablename__ = 'transaction'

    transaction_date = Column(String(length=60), nullable=False, default=datetime.utcnow())
    PAYMENT_CHOICES =['Card', 'Cash']
    payment_method = Column(Enum(*PAYMENT_CHOICES, name='payment_enum'), nullable=False)
    TRANSACTION_CHOICES =['Pending', 'Approved']
    transaction_status = Column(Enum(*TRANSACTION_CHOICES, name='transact_enum'), nullable=False)
    total_amount = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates="transaction")
    order = relationship('Order', back_populates='transaction')