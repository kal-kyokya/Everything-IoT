#!/usr/bin/python3
"""
'user' declare and define the DB table storing user's infos
"""
# Import necessary modules
from datetime import datetime
from models.base_model import Base, BaseModel
import sqlalchemy
from sqlalchemy import Column, Date, DataTime, String


# Create the class
class User(BaseModel, Base):
    """Class to be mapped to the 'User' database table."""
    __tablename__ = 'user'
    email = Colum(String(45), nullable=False, unique=True)
    username = Column(String(45), nullable=False, unique=True)
    Firstname = Column(String(45), nullable=False)
    lastname = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)
