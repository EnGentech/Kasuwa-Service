from sqlalchemy import Column, String, Integer, ForeignKey, Float, LargeBinary
from models.baseModels import BaseModel, Base
from sqlalchemy.orm import relationship

class Product(BaseModel, Base):
    """Populating products in database"""
    __tablename__ = 'products'
    category_id = Column(Integer, ForeignKey('categories.id'))
    product_name = Column(String(20), nullable=False)
    product_type = Column(String(200), nullable=False)
    description = Column(String(200), nullable=False)
    stock = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    image_source = Column(String(255), nullable=False)
    category = relationship("Category", back_populates="products")
    carts = relationship('Cart', back_populates='products', cascade='all, delete-orphan')
    transactions = relationship('Transaction', back_populates='products', cascade='all, delete-orphan')
    comments = relationship('Comment', back_populates='products')
    ratings = relationship('Rating', back_populates='products')