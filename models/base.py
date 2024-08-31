#!/usr/bin/python3
"""
'base_model' lays out the blueprint for all database tables
"""
# Import the necessary modules and/or tools
from datetime import datetime
import models
import sqlalchemy
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import uuid


# Instanciate the object used to create and delete database tables
Base = declarative_base()

# Time format to be used when generating datetime objects off of strings
time_format = "%a %d %b %Y, %H:%M:%S"


# Define the BaseModel class (A database table itself)
class BaseModel:
    """Defines attributes and methods common to all DB tables."""

    # Define the table columns
    id = Column(String(25), primary_key=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    # Define the '__init__' method
    def __init__(self, *args, **kwargs):
        """Automatically called when a BaseModel object is created."""
        # If user pass a dict ('key:word' args) off of which to make the object
        if kwargs:
            # Parse input values and create object accordingly
            for key, value in kwargs.items():
                if key != 'class':
                    setattr(self, key, value)

            if kwargs.get('id', None) is None:
                self.id = str(uuid.uuid4())
            if kwargs.get('created_at', None) is None:
                self.created = datetime.utcnow()
            elif type(self.created_at) is str:
                self.__created_at = datetime.strptime(value, time_format)
            if kwargs.get('updated_at', None) is None:
                self.updated_at = datetime.utcnow()
            elif type(self.updated_at) is str:
                self.__updated_at = datetime.strptime(value, time_format)

        else:
            # Initialize the 3 compulsory attributes of all objects
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated = datetime.now()

    # Define additional methods
    def __str__(self):
        """Overwrites the built-in string representation for class objects."""
        return ("This is a {}, created on {}\nid: {}".format(
            self.__class__.__name__, self.created_at, self.id))

    def to_dict(self):
        """Generates a dictionary representation of the object."""
        # Create a copy of the python dictionary representation of the object
        my_dict = self.__dict__.copy()

        # Remove the password attribute if it exists
        if 'password' in my_dict.keys():
            del my_dict['password']

        # Add the class name to the dictionary to be returned
        my_dict['class'] = self.__class__.__name__

        # Convert datetime objects into user friendly strings
        if my_dict.get('created_at'):
            my_dict['created_at'] = my_dict['created_at'].strftime(time_format)
        if my_dict.get('updated_at'):
            my_dict['updated_at'] = my_dict['updated_at'].strftime(time_format)
        return my_dict
