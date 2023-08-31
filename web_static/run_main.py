from sqlalchemy import engine, create_engine
from models.baseModels import Base
from sqlalchemy.orm import sessionmaker
from models.category import Category
from models.cart import Cart
from models.comment import Comment
from models.product import Product
from models.rating import Rating
from models.transaction import Transaction
from models.user import User

# Create a new SQLAlchemy engine and session
url = "mysql+mysqldb://root:admin8634@localhost/kasuwa" 
engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
