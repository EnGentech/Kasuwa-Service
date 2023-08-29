from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from base import Base, BaseModel


class Order(BaseModel, Base):
    __tablename__ = 'orders'

    shipping_address_id = Column(Integer, ForeignKey('billing_address.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates='order')
    shipping_address = relationship('BillingAddress')
    transaction_id = Column(Integer, ForeignKey('transaction.id'))
    transaction = relationship('Transaction', back_populates='order')
    order_item_id  = Column(Integer, ForeignKey('order_items.id'))
    order_item = relationship('OrderItem', back_populates='order')