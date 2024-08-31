#!/usr/bin/python3
"""
'db_storage' contains the script for the creation of the database
"""
# Import the necessary modules
from models.base import Base
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


# Create the the class that allows object relational mapping
class DBStorage:
    """Objects of this class can be bound to database engines."""

    __engine = None
    __session = None

    # Use init dunder to initialize the engine class attribute
    def __init__(self):
        """Creates a database engine off of environment variables."""
        # Get the environment variables
        USERNAME = getenv('EIOT-USERNAME')
        PWD = getenv('EIOT-PWD')
        HOST = getenv('EIOT-HOST')
        DB_NAME = getenv('EIOT-DB_NAME')
        DB_ENV = getenv('EIOT-DB_ENV')

        # Create the database engine
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(USERNAME, PWD,
                                             HOST, DB_NAME))

        # Delete all the tables if the DB used is for testing new features
        if DB_ENV == 'test':
            Base.metadata.drop_all(engine)

    # Populate DB with previously stored data and avail a session object
    def remember(self):
        """Reloads records committed during past sessions."""
        # Recreate all previously defined tables and load their content
        Base.metadata.create_all(engine)

        # Create a class whose objects can manipulate the 'engine' database
        Session = sessionmaker(bind=engine)

        # Wrap the class and enable thread-safe management of session objects
        safeSession = scoped_session(Session)

        # Initialize the class attribute 'session'
        self.__session = safeSession()

    # Additional useful methods for CRUD Operations
    def create(self, obj):
        """Add a new database record; 'C' in CRUD.
        Arg:
            obj - The object representing the created record.
        """
        self.__session.add(obj)

    def delete(self, obj):
        """Removes a database row; 'D' in CRUD.
        Arg:
            obj - The object to be deleted."""
        self.__session.remove(obj)

    def commit(self):
        """Register changes made to the DB, e.g;  In CRUD, a 'U' operation."""
        self.__session.commit()
