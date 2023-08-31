from sqlalchemy import Table, Column, String, Integer, Date, Enum
from .Base_connect import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin

class User(Base, UserMixin):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(length=50), nullable=False)
    fullname = Column(String(length=50), nullable=False)
    email = Column(String(length=50), unique=True,
    nullable=False)
    password = Column(String(length=150))
    address = Column(String(length=200))
    phone = Column(String(length=20))  
    GENDER_CHOICES = ['male', 'female']
    gender = Column(Enum(*GENDER_CHOICES, name='gender_enum'))
    birthDate = Column(Date)
    comments = relationship("Comment", back_populates="user")
    ratings = relationship("Rating")
    billing_address = relationship("Billing_address", back_populates="user")
    carts = relationship("Cart", back_populates="user")
    products = relationship("Product", back_populates="user", primaryjoin="User.id == Product.user_id")
    transactions = relationship("Transaction")
    orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"<User {self.fullname}>"

class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True)
    comment = Column(String(length=200))
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    user = relationship("User", back_populates="comments")
    category = relationship("Category", back_populates="comments")
    product = relationship("Product", back_populates="comments")

    def __repr__(self):
        return f"<C {self.comment}>"
    
products_Transactions = Table('product_trans', 
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('transaction_id', Integer, ForeignKey('transactions.id'))
)

cart_prod = Table('cart_product', 
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('cart_id', Integer, ForeignKey('carts.id'))
)

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    type = Column(String(20), nullable=False)
    description = Column(String(200), nullable=False)
    stock = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    transaction = relationship("Transaction",secondary=products_Transactions, overlaps="transaction")
    cart = relationship("Cart", secondary=cart_prod, overlaps="cart")
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="products")
    comments = relationship("Comment", back_populates="product")
    image_source = Column(String(225))
    order = relationship("Order", back_populates="product")

    def __repr__(self):
        return f"<Productname {self.name}>"
    
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="transactions")
    product = relationship("Product", secondary=products_Transactions, overlaps="transaction")
    category = relationship("Category")
    category_id = Column(Integer, ForeignKey('categories.id'))
    quantity = Column(Integer)
    approval_status = Column(String(10), nullable=False)
    orders = relationship("Order", back_populates="transaction")

    def __repr__(self):
        return f"<User {self.__name__}>"


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    category = Column(String(15))
    ratings = relationship("Rating", back_populates="category")
    cart = relationship("Cart", back_populates="category")
    comments = relationship("Comment", back_populates="category")
    orders = relationship("Order", back_populates="category")

    def __repr__(self):
        return f"<User {self.__name__}>"

class Cart(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="carts")
    product = relationship("Product", secondary=cart_prod, overlaps="cart")
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="cart")
    cart = relationship("Product", secondary=cart_prod, overlaps="product")
    quantity = Column(Integer)

    def __repr__(self):
        return f"<User {self.quantity}>"
class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="ratings")
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product")
    user = relationship("User", back_populates="ratings")
    value = Column(Integer)

    def __repr__(self):
        return f"<User {self.value}>"
    
class Billing_address(Base):
    __tablename__ = "billing_address"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")
    bill_address = Column(String(45), nullable=False)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    transaction_id = Column(Integer, ForeignKey('transactions.id'))
    category_id = Column(Integer, ForeignKey("categories.id"))
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))

    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="order")
    category = relationship("Category", back_populates="orders")
    transaction = relationship("Transaction", back_populates="orders")
