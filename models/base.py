import sqlite3
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer



app = Flask(__name__)
db_uri = 'sqlite:///kasuwa.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    
    id = Column(Integer, primary_key=True)
engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)