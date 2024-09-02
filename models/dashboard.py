#!/usr/bin/python3
"""
'dashboard' declares and defines the Dashboard table of our database
"""
# Import the necessary modules and/or utilities
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


# Define the table
class Dashboard(BaseModel, Base):
    """Contains informations about all the dashboards.
    Parent classes:
        BaseModel: Contains methods common to all database tables.
        Base: Contains the utility mapping classes to database tables.
    """
    # Define the name to be used during table creation by the database
    __tablename__ = "Dashboard"

    # Define the table's columns
    Name = Column(String(45), nullable=False, unique=True)

    # Establish a one to many relationship with the microcontroller table
    Microcontrollers = relationship('Microcontroller',
                                    back_populates='Dashboard')

    # Establish a many to one relationship with the user table
    User_id = Column(String(45), ForeignKey('User.id'))
    Owner = relationship('User', back_populates='Dashboard')

    # Set up the __init__ method
    def __init__(self, *args, **kwargs):
        """Called whenever a new Dashboard object is instanciated."""
        # Use the init method declared in the inherited BaseModel
        super().__init__(*args, **kwargs)
