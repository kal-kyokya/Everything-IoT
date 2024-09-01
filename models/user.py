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
    # Define the name the table will be registered under in the DB.
    __tablename__ = 'User'

    # Define the columns to be found in the table
    Email = Colum(String(45), nullable=False, unique=True)
    Username = Column(String(45), nullable=False, unique=True)
    Firstname = Column(String(45), nullable=False)
    Lastname = Column(String(45), nullable=False)
    Password = Column(String(45), nullable=False)
    Sex = Column(String(45), nullable=True)
    Phone = Column(String(45), nullable=True)
    Country = Column(String(45), nullable=True)
    City = Column(String(45), nullable=True)
    Birthday = Column(Date(), nullable=True)

    # Set up the __init__ method
    def __init__(self):
        """Called whenever a new object of type User is created."""
        pass
