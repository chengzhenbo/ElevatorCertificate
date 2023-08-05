from sqlalchemy import Column, text, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()

class Book(Base):
    __tablename__ = 'book'
    id  = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    rating = Column(Float)
    price = Column(Float, server_default=text('1'))

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

