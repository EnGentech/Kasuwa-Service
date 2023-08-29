from associations import comment_on_products
from sqlalchemy import Column, String, Float, Text, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from base import Base, BaseModel


# import json


class Product(BaseModel, Base):
    __tablename__ = 'product'

    product_name = Column(String(length=250), nullable=False)
    description = Column(Text, nullable=False)
    specification = Column(Text, nullable=False)
    stock = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    image_url = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    categories = relationship("Category", back_populates='product')
    ratings = relationship("Rating", back_populates='product', cascade="all, delete-orphan")
    comments = relationship('Comments', secondary=comment_on_products, back_populates='products')