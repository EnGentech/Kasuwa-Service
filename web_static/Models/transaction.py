from sqlalchemy import Column, String, Integer, ForeignKey
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