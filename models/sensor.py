#!/usr/bin/python3
"""
'sensor' declares and define the Sensor table of our database
"""
# Import the necessary modules and/or utilities
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


# Define the table
class Sensor(BaseModel, Base):
    """Contains informations about sensors found in circuitries.
    Parent classes:
        BaseModel: Contains methods common to all database tables.
        Base: Contains the utility mapping classes to database tables.
    """
    # Define the name to be used during table creation by the database
    __tablename__ = "Sensor"

    # Define the table's columns
    Name = Column(String(45), nullable=False, unique=True)

    # Establish a many to one relationship with the microcontroller table
    Microcontroller_id = Column(String(45), ForeignKey('Microcontroller.id'))
    Controller = relationship('Microcontroller', back_populates='Sensor')

    # Establish a many to one relationship with the type table
    Type_id = Column(String(45), ForeignKey('Type.id'))
    Sensor_type = relationship('Type', back_populates='Sensor')

    # Establish a many to one relationship with the location table
    Location_id = Column(String(45), ForeignKey('Location.id'))
    Sensor_location = relationship('Location', back_populates='Sensor')

    # Set up the __init__ method
    def __init__(self, *args, **kwargs):
        """Called whenever a new Sensor Instance comes to life."""
        # Use the init method declared in the inherited BaseModel
        super().__init__(*args, **kwargs)
