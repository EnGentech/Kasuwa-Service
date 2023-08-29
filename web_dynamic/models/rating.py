from sqlalchemy import Column, String, Integer, Float, ForeignKey
from base import Base, BaseModel
from sqlalchemy.orm import relationship


class Rating(BaseModel, Base):
    __tablename__ = 'rating'

    rating = Column(Float, nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    product = relationship("Product", back_populates="ratings")
    user = relationship("User", back_populates='ratings')
