#!/usr/bin/python3
"""
'thing' declares and defines the Thing table of our database
"""
# Import the necessary modules and/or utilities
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Boolean, Column, String, ForeignKey
from sqlalchemy.orm import relationship


# Define the table
class Thing(BaseModel, Base):
    """Contains informations about each present electronic component.
    Parent classes:
        BaseModel: Contains methods common to all database tables.
        Base: Contains the utility mapping classes to database tables.
    """
    # Define the name to be used during table creation by the database
    __tablename__ = "things"

    # Define the table's columns
    name = Column(String(45), nullable=False, unique=True)
    state = Column(Boolean(), nullable=False)

    # Establish a many to one relationship with the microcontroller table
    microcontroller_id = Column(String(45), ForeignKey('microcontrollers.id'))
    controller = relationship('Microcontroller',
                              back_populates='things',
                              cascade='delete')

    # Establish a many to one relationship with the location table
    location_id = Column(String(45), ForeignKey('locations.id'))
    thing_location = relationship('Location',
                                  back_populates='things',
                                  cascade='delete')

    # Establish a many to one relationship with the type table
    type_id = Column(String(45), ForeignKey('types.id'))
    thing_type = relationship('Type',
                              back_populates='things',
                              cascade='delete')

    # Set up the __init__ method
    def __init__(self, *args, **kwargs):
        """Called whenever a new object of class Thing is made."""
        # Use the init method declared in the inherited BaseModel
        super().__init__(*args, **kwargs)
