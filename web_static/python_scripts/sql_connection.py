from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create a new SQLAlchemy engine and session
url = "mysql+mysqldb://root:admin8634@localhost/kasuwa" 
engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Define a base class for declarative models
Base = declarative_base()