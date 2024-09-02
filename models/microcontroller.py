#!/usr/bin/python3
"""
'microcontroller' declares and defines the database Microcontroller table
"""
# Import the necessary modules and/or utilities
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


# Define the table
class Microcontroller(BaseModel, Base):
    """Each associated instance represents a microcontroller.
    Parent classes:
        BaseModel: Contains methods used by all database tables.
        Base: Possesses the utility mapping classes to database tables.
    """
    # Define the name to be used during table creation by the database
    __tablename__ = "Microcontroller"

    # Define the table's columns
    Name = Column(String(45), nullable=False, unique=True)
    Model = Column(String(45), nullable=False)
    Status = Column(String(45), nullable=False)

    # Establish a many to one relationship with the dashboard table
    Dashboard_id = Column(String(45), ForeignKey('Dashboard.id'))
    Board = relationship('Dashboard', back_populates='Microcontroller')

    # Establish a many to one relationship with the location table
    Location_id = Column(String(45), ForeignKey('Location.id'))
    Controller_location = relationship('Location',
                                       back_populates='Microcontroller')

    # Establish one to many relationships with the Sensor and Thing tables
    Sensors = relationship('Sensor', back_populates='Microcontroller')
    Things = relationship('Thing', back_populates='Microcontroller')

    # Set up the __init__ method
    def __init__(self, *args, **kwargs):
        """Called whenever a new microcontroller object is created."""
        # Use the init method declared in the inherited BaseModel
        super().__init__(*args, **kwargs)
