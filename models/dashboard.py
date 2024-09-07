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
    __tablename__ = "dashboards"

    # Define the table's columns
    name = Column(String(45), nullable=False, unique=True)

    # Establish a one to many relationship with the microcontroller table
    microcontrollers = relationship('Microcontroller',
                                    back_populates='board',
                                    cascade='delete')

    # Establish a many to one relationship with the user table
    user_id = Column(String(45), ForeignKey('users.id'))
    owner = relationship('User',
                         back_populates='dashboards',
                         cascade='delete')

    # Set up the __init__ method
    def __init__(self, *args, **kwargs):
        """Called whenever a new Dashboard object is instanciated."""
        # Use the init method declared in the inherited BaseModel
        super().__init__(*args, **kwargs)
