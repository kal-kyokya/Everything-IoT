#!/usr/bin/python3
"""
'user' declares and defines the DB table storing user's infos
"""
# Import necessary modules
from flask_login import UserMixin
from datetime import datetime
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Date, String
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash


# Create the class
class User(BaseModel, Base, UserMixin):
    """Class to be mapped to the 'User' database table.
    Parent classes:
        BaseModel: Contains methods shared by all database tables .
        Base: Contains the utility mapping classes to database tables.
        UserMixin: Enables user tracking by flask's login manager
    """
    # Define the name the table will be registered under in the DB.
    __tablename__ = 'users'

    # Define the columns to be found in the table
    email = Column(String(45), nullable=False, unique=True)
    username = Column(String(45), nullable=False, unique=True)
    firstname = Column(String(45), nullable=False)
    lastname = Column(String(45), nullable=False)
    password = Column(String(256), nullable=False)
    sex = Column(String(45), nullable=True)
    phone = Column(String(45), nullable=True)
    country = Column(String(45), nullable=True)
    city = Column(String(45), nullable=True)
    birthday = Column(Date(), nullable=True)

    # Establish one to many relationship with the Dashboard table
    dashboards = relationship('Dashboard', back_populates='owner')

    # Set up the __init__ method
    def __init__(self, *args, **kwargs):
        """Called whenever a new object of type User is created."""
        # Use the init method declared in the inherited BaseModel
        super().__init__(*args, **kwargs)

        # Make sure the user password is not stored in plain text
        if self.password:
            # Use a hashing function to encrypt and thus secure the password
            self.password = generate_password_hash(self.password,
                                                   method='pbkdf2:sha256',
                                                   salt_length=8)
