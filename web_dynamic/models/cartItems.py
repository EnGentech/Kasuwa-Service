from base import Base, BaseModel
from sqlalchemy import Integer, String, Float, ForeignKey, Column
from sqlalchemy.orm import relationship


class CartItems(BaseModel, Base):
    __tablename__ = 'cart_items'

    quantity = Column(Integer, nullable=False)
    # cart_id = Column(Integer, ForeignKey('cart.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    cart = relationship("Cart", back_populates='items',  cascade="all, delete-orphan")
    product = relationship("Product")