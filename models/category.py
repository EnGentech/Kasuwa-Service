from base import Base, BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



class Category(BaseModel, Base):
    __tablename__ ='category'
    
    title = Column(String(200), nullable=False)
    product = relationship('Product', back_populates='categories', cascade="all, delete-orphan")
