from associations import comment_on_products
from base import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



class Comments(BaseModel, Base):
    __tablename__ = 'comment'

    message = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='comments')
    products = relationship('Product', secondary=comment_on_products, cascade="all, delete", back_populates='comments')