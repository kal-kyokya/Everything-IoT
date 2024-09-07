#!/usr/bin/python3
"""
'location' declares and defines the Location table of our database
"""
# Import the necessary modules and/or utilities
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


# Define the table
class Location(BaseModel, Base):
    """Contains informations about the various monitored locations.
    Parent classes:
        BaseModel: Contains methods common to all database tables.
        Base: Contains the utility mapping classes to database tables.
    """
    # Define the name to be used during table creation by the database
    __tablename__ = "locations"

    # Define the table's columns
    name = Column(String(45), nullable=False, unique=True)
    description = Column(String(45), nullable=False)

    # Establish a one to many relationsip with database tables
    microcontrollers = relationship('Microcontroller',
                                    back_populates='controller_location',
                                    cascade='delete')
    things = relationship('Thing',
                          back_populates='thing_location',
                          cascade='delete')
    sensors = relationship('Sensor',
                           back_populates='sensor_location',
                           cascade='delete')

    # Set up the __init__ method
    def __init__(self, *args, **kwargs):
        """Called whenever a new object of class Location is created."""
        # Use the init method declared in the inherited BaseModel
        super().__init__(*args, **kwargs)
