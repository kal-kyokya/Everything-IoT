#!/usr/bin/python3
"""
'user' declares and defines the DB table storing user's infos
"""
# Import necessary modules
from datetime import datetime
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Date, DataTime, String
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash


# Create the class
class User(BaseModel, Base):
    """Class to be mapped to the 'User' database table.
    Parent classes:
        BaseModel: Contains methods shared by all database tables .
        Base: Contains the utility mapping classes to database tables.
    """
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

    # Establish one to many relationship with the Dashboard table
    Dashboards = relationship('Dashboard', back_populates='User')

    # Set up the __init__ method
    def __init__(self, *args, **kwargs):
        """Called whenever a new object of type User is created."""
        # Use the init method declared in the inherited BaseModel
        super().__init__(*args, **kwargs)

        # Make sure the user password is not stored in plain text
        if self.Password:
            # Use a hashing function to encrypt and thus secure the password
            self.Password = generate_password_hash(self.Password,
                                                   method='pbkdf2:sha256',
                                                   salt_length=8)
