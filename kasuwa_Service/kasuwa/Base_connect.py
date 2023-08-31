from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker, Mapped
from sqlalchemy.ext.declarative import declarative_base
import sqlite3

db = sqlite3.connect('kasuwa.db')
db_uri = 'sqlite:///kasuwa.db'

engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
print('here we go')