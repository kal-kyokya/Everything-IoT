#!/usr/bin/python3
"""
'type' declares and defines the Type table of our database
"""
# Import the necessary modules and/or utilities
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


# Define the table
class Type(BaseModel, Base):
    """Contains descriptions of the different types of sensor and thing.
    Parent classes:
        BaseModel: Contains methods common to all database tables.
        Base: Contains the utility mapping classes to database tables.
    """
    # Define the name to be used during table creation by the database
    __tablename__ = "types"

    # Define the table's columns
    name = Column(String(45), nullable=False, unique=True)
    description = Column(String(79), nullable=False)

    # Establish one to many relationships with database tables
    things = relationship('Thing',
                          back_populates='thing_type',
                          cascade='delete')
    sensors = relationship('Sensor',
                           back_populates='sensor_type',
                           cascade='delete')

    # Set up the __init__ method
    def __init__(self, *args, **kwargs):
        """Called whenever a new Type object is made."""
        # Use the init method declared in the inherited BaseModel
        super().__init__(*args, **kwargs)
