#!/usr/bin/python3
"""
'work' creates a web app blueprint handling a section named projects
"""
# Alphabetically ordered list of imported modules
from flask import Blueprint, render_template


# Create the blueprint
project_bp = Blueprint('project', __name__)


# Define various associated routes and handlers
@project_bp.route('/projects')
def projects():
    """Handles any request to the above url."""
    return render_template("projects.html")
