#!/usr/bin/python3
"""
'work' creates a web app blueprint handling a section named projects
"""
# Alphabetically ordered list of imported modules
from flask import Blueprint, render_template
from flask_login import current_user


# Create the blueprint
project_bp = Blueprint('project', __name__)


# Define various associated routes and their handlers
@project_bp.route('/projects')
def projects():
    """Handles any request to the 'projects' url."""
    return render_template("projects.html")


@project_bp.route('/account')
def account():
    """Handles any request to the 'account' secondary nav-bar link."""
    return render_template("account.html", user=current_user)


@project_bp.route('/dashboards')
def dashboards():
    """Handles any request to the 'dashboards' secondary nav-bar link."""
    return render_template("dashboards.html")


@project_bp.route('/monitors')
def monitors():
    """Handles any request to the 'monitors' secondary nav-bar link."""
    return render_template("monitors.html")


@project_bp.route('/alerts')
def alerts():
    """Handles any request to the 'alerts' secondary nav-bar link."""
    return render_template("alerts.html")


@project_bp.route('/theme')
def theme():
    """Handles any request to the 'theme' secondary nav-bar link."""
    return render_template("theme.html")


@project_bp.route('/help')
def help():
    """Handles any request to the 'help' secondary nav-bar link."""
    return render_template("help.html")


@project_bp.route('/recent')
def recent():
    """Handles any request to the 'recent' secondary nav-bar link."""
    return render_template("recent.html")


@project_bp.route('/create')
def create():
    """Handles any request to the 'create' secondary nav-bar link."""
    return render_template("create.html")
