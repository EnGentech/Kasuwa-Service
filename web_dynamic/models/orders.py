from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.baseModels import BaseModel, Base

class OrderItems(BaseModel, Base):
    """creating order items table"""
    __tablename__ = "order_items"
    transaction_id = Column(Integer, ForeignKey('transactions.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    item = Column(String(60), nullable=False)