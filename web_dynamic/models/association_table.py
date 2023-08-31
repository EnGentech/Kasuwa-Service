from product import Product
from transaction import Transaction
from sqlalchemy import Table, Column, Integer, ForeignKey
from baseModels import Base
from category import Category
from orders import OrderItems

cat_prod = Table('category_product', Base.metadata,
                Column('product_id', Integer, ForeignKey('products.id')),
                Column('category_id', Integer, ForeignKey('categories.id'))
                 )

ord_prod = Table('order_product', Base.metadata, 
                Column('order_id', Integer, ForeignKey('order_items.id')),
                Column('product_id', Integer, ForeignKey('products.id'))
                 )

trans_prod = Table('transaction_products', Base.metadata,
                   Column('transactions_id', Integer, ForeignKey('transactions.id')),
                   Column('products_id', Integer, ForeignKey('products.id'))
                   )