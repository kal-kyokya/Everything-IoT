#!usr/bin/python3
"""
'routes' defines endpoints available to the user as well as handlers.
"""
# List of imported modules
from flask import Blueprint, render_template
from flask_login import login_required, current_user


# Declare this file as one of the Blueprints of the flask web app
home_bp = Blueprint('home', __name__)


# Endpoint definitions
@home_bp.route('/')
def home():
    """Landing page of the web application."""
    return render_template('logged_out.html')


@home_bp.route('/home')
@login_required
def loggedIn():
    """Home page as seen by any logged in user."""
    return render_template('logged_in.html', user=current_user)
