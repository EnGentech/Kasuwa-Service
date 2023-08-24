from sqlalchemy import Column, String, Integer, ForeignKey, Float, LargeBinary
from models.baseModels import BaseModel, Base

class Product(BaseModel, Base):
    """Populating products in database"""
    __tablename__ = 'products'
    category_id = Column(Integer, ForeignKey('categories.id'))
    product_name = Column(String(20), nullable=False)
    product_type = Column(String(200), nullable=False)
    description = Column(String(200), nullable=False)
    stock = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    image_source = Column(LargeBinary, nullable=False)