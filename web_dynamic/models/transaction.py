from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.baseModels import BaseModel, Base

class Transaction(BaseModel, Base):
    """Class for transaction"""
    __tablename__ = 'transactions'
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    transaction_id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    approval_status = Column(String(10), nullable=True)
    users = relationship('User', back_populates='transactions')
    products = relationship('Product', back_populates='transactions')
    order_items = relationship('OrderItems', back_populates='transactions')
    