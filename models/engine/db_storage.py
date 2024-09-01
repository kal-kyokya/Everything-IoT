#!/usr/bin/python3
"""
'db_storage' contains the script for the creation of the database
"""
# Import the necessary modules
from models.base_model import Base
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


# List the DB tables in a dict for easier retrieval
classes = {'User': User, 'Dashboard': Dashboard,
           'Microcontroller': Microcontroller,
           'Location': Location, 'Thing': Thing,
           'Type': Type, 'Sensor': Sensor}


# Create the the class that allows object relational mapping
class DBStorage:
    """Objects of this class can be bound to database engines."""

    __engine = None
    __session = None

    # Use init dunder to initialize the engine class attribute
    def __init__(self):
        """Creates a database engine off of environment variables."""
        # Get the environment variables
        USERNAME = getenv('EIOT_USERNAME')
        PWD = getenv('EIOT_PWD')
        HOST = getenv('EIOT_HOST')
        DB_NAME = getenv('EIOT_DB_NAME')
        DB_ENV = getenv('EIOT_DB_ENV')

        # Create the database engine
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(USERNAME, PWD,
                                             HOST, DB_NAME))

        # Delete all the tables if the DB used is for testing new features
        if DB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    # Populate DB with previously stored data and avail a session object
    def remember(self):
        """Reload records created during past sessions."""
        # Recreate all previously defined tables and load their content
        Base.metadata.create_all(self.__engine, echo=True)

        # Create a class whose objects can manipulate the 'engine' database
        Session = sessionmaker(bind=self.__engine)

        # Wrap the class and enable thread-safe management of session objects
        safeSession = scoped_session(Session)

        # Initialize the 'session' attribute by instanciating safeSession
        self.__session = safeSession()

    # Additional useful methods for CRUD Operations
    def add(self, obj):
        """Add a new database record; 'C' in CRUD.
        Arg:
            obj - The object representing the created record.
        """
        self.__session.add(obj)

    def commit(self):
        """Register changes made to the DB, e.g;  In CRUD, a 'U' operation."""
        self.__session.commit()

    def delete(self, obj):
        """Remove a database row; 'D' in CRUD.
        Arg:
            obj - The object to be deleted."""
        self.__session.delete(obj)

    def all(self, cls=None):
        """Request a set of records from the current database session"""
        new_dict = {}
        for clss in classes:
            if (cls is None) or (cls is classes[clss]) or (cls is clss):
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def get(self, cls, id):
        """Retrieve an object based on its classname and ID.
        Args:
            cls: String, name of the class to which object belongs.
            id: Integer, Unique Identifier of the object
        Return:
            The actual Object or None, if not found.
        """
        try:
            if cls is None or id is None or not isinstance(id, str):
                print("Usage: obj.get(<className>, <ID>)")
            else:
                for clss in classes:
                    if cls == clss or cls == classes[clss]:
                        objs_dict = self.all(cls)
                        for obj in objs_dict.values():
                            if id == obj.id:
                                return (obj)
                        return (None)
        except Exception:
            print("Error occured during 'get()' call.")

    def count(self, cls=None):
        """Compute the number of Objects in storage.
        Arg:
            cls: Optional, specify the className filter.
        Return:
            The number of objects found in storage.
        """
        if cls is None:
            objs_list = self.all().values()
            return (len(objs_list))
        count = 0
        for obj in self.all().keys():
            class_name = obj.split('.')[0]
            if class_name == cls:
                count += 1
        return (count)

    def close(self):
        """End the current database session."""
        self.__session.remove()
