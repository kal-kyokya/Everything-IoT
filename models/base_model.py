#!/usr/bin/python3
"""
'base_model' lays out the blueprint for all database tables
"""
# Import the necessary modules and/or tools
from datetime import datetime
import models
import sqlalchemy
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
import uuid


# Instanciate the object used to create and delete database tables
Base = declarative_base()

# Time format to be used when generating datetime objects off of strings
time_format = "%a %d %b %Y, %H:%M:%S"


# Define the BaseModel class (A database table itself)
class BaseModel:
    """Define attributes and methods common to all DB tables."""

    # Define the must-have columns of all tables
    id = Column(String(45), primary_key=True)
    created_on = Column(DateTime(), nullable=False, default=datetime.now)
    updated_on = Column(DateTime(), nullable=False, default=datetime.now)

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
            if kwargs.get('created_on', None) is None:
                self.created = datetime.now()
            elif type(self.created_on) is str:
                self.__created_on = datetime.strptime(value, time_format)
            if kwargs.get('updated_on', None) is None:
                self.updated_on = datetime.now()
            elif type(self.updated_on) is str:
                self.__updated_on = datetime.strptime(value, time_format)

        else:
            # Initialize the 3 compulsory attributes of all objects
            self.id = str(uuid.uuid4())
            self.created_on = datetime.now()
            self.updated_on = datetime.now()

    # Define additional methods
    def save(self):
        """Store the associated object inside our database."""
        self.updated_on = datetime.now()
        models.storage.add(self)
        models.storage.commit()

    def delete(self):
        """Remove the instance from the database storage"""
        models.storage.delete(self)

    def __str__(self):
        """Overwrite the __str__ built-in method.
        '__str__' provides a string representation more readable for humans."""
        return ("This is a {}, created on {}\nid: {}".format(
            self.__class__.__name__, self.created_on, self.id))

    def __repr__(self):
        """Overwrite the __repr__ built-in method.
        '__repr__' is for unambiguous string representation for developers."""
        return ("{} {}\n".format(
            upper(self.__class__.__name__), self.created_on, self.id))

    def to_dict(self):
        """Generate a dictionary representation of the object."""
        # Create a copy of the python dictionary representation of the object
        my_dict = self.__dict__.copy()

        # Remove the password attribute if it exists
        if 'password' in my_dict.keys():
            del my_dict['password']

        # Add the class name to the dictionary to be returned
        my_dict['class'] = self.__class__.__name__

        # Convert datetime objects into user friendly strings
        if my_dict.get('created_on'):
            my_dict['created_on'] = my_dict['created_on'].strftime(time_format)
        if my_dict.get('updated_on'):
            my_dict['updated_on'] = my_dict['updated_on'].strftime(time_format)
        return my_dict
