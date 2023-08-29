from base import Base
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base



# transactions_products_association = Table(
#     'transaction_products', Base.metadata,
#     Column('transaction_id', Integer, ForeignKey('transaction.id')),
#     Column('products_id', Integer, ForeignKey('product.id'))
# )

comment_on_products = Table(
    'comment_product', Base.metadata,
    Column('comment_id', Integer, ForeignKey('comment.id')),
    Column('product_id', Integer, ForeignKey('product.id'))
)