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
    created_on = Column(DateTime(), nullable=False, default=datetime.now())
    updated_on = Column(DateTime(), nullable=False, default=datetime.now())

    # Define the '__init__' method
    def __init__(self, *args, **kwargs):
        """Instantiation of new BaseModel Class"""
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid4())
            self.created_on = datetime.utcnow()
            self.updated_on = self.created_on

    def __set_attributes(self, input_dict):
        """private: converts input_dict values to python class attributes"""
        if 'id' not in input_dict:
            input_dict['id'] = str(uuid.uuid4())
        if 'created_on' not in input_dict:
            input_dict['created_on'] = datetime.utcnow()
        elif not isinstance(input_dict['created_on'], datetime):
            input_dict['created_on'] = datetime.strptime(input_dict['created_on'],
                                                        time_format)
        if 'updated_at' not in input_dict:
            input_dict['updated_at'] = datetime.utcnow()
        elif not isinstance(input_dict['updated_at'], datetime):
            input_dict['updated_at'] = datetime.strptime(input_dict['updated_at'],
                                                        time_format)
        for attr, val in input_dict.items():
            setattr(self, attr, val)

    # Define additional methods
    def update(self, new_values=None):
        """Update a class and sets allowed attributes"""
        IGNORE = ['id', 'created_on', 'updated_on',
                  'Email', 'Username', 'Password']

        # Check that the dictionary of new attributes is availed
        if new_values:
            updated_dict = {
                k: v for k, v in new_values.items() if k not in IGNORE
            }

            for key, value in updated_dict.items():
                setattr(self, key, value)

            self.save()

    def delete(self):
        """Remove the instance from the database storage"""
        models.storage.delete(self)

    def save(self):
        """Store the associated object inside our database."""
        self.updated_on = datetime.now()
        models.storage.add(self)
        models.storage.commit()

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

    def __str__(self):
        """Overwrite the __str__ built-in method.
        '__str__' provides a string representation more readable for humans."""
        return ("This is a {}, created on {}\nid: {}".format(
            self.__class__.__name__, self.created_on, self.id))
