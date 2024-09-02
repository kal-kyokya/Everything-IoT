#!/usr/bin/python3
"""
This file contains an instance of the storage engine.
Instance to be imported by:
    Each module that manipulate the engine.
"""
# Import the necessary modules
from models.engine.db_storage import DBStorage


# Instanciate the storage engine
storage = DBStorage()

# Reloads past session content
storage.remember()
