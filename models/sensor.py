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
    __tablename__ = "sensors"

    # Define the table's columns
    name = Column(String(45), nullable=False, unique=True)

    # Establish a many to one relationship with the microcontroller table
    microcontroller_id = Column(String(45), ForeignKey('microcontrollers.id'))
    controller = relationship('Microcontroller',
                              back_populates='sensors',
                              cascade='delete')

    # Establish a many to one relationship with the type table
    type_id = Column(String(45), ForeignKey('types.id'))
    sensor_type = relationship('Type',
                               back_populates='sensors',
                               cascade='delete')

    # Establish a many to one relationship with the location table
    location_id = Column(String(45), ForeignKey('locations.id'))
    sensor_location = relationship('Location',
                                   back_populates='sensors',
                                   cascade='delete')

    # Set up the __init__ method
    def __init__(self, *args, **kwargs):
        """Called whenever a new Sensor Instance comes to life."""
        # Use the init method declared in the inherited BaseModel
        super().__init__(*args, **kwargs)
