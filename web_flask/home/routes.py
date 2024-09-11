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
@home_bp.route('/home')
def home():
    """Landing page of the web application."""
    if current_user.is_authenticated:
        return render_template('logged_in.html', user=current_user)
    return render_template('logged_out.html')    


@home_bp.route('/services/<service>')
def services(service):
    """Return specific content based on a clicked service."""
    return render_template('service.html',
                           service=service,
                           user=current_user)


@home_bp.route('/solutions')
def solutions():
    """Return the web page associated with the 'solutions' nav-bar link."""
    return render_template('solution.html')


@home_bp.route('/blog')
def blog():
    """Page associated with the 'blog' nav-bar link."""
    return render_template('blog.html')


@home_bp.route('/about')
def about():
    """Web page associated with the 'about' nav-bar link."""
    return render_template('about.html')
