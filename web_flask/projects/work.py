#!/usr/bin/python3
"""
'work' creates a flask app blueprint handling the 'projects' section
"""
# Alphabetically ordered list of imported modules
from flask import Blueprint, render_template
from flask_login import login_required, current_user


# Create the blueprint
project_bp = Blueprint('project', __name__)


# Define various associated routes and their handlers
@project_bp.route('/projects')
@login_required
def projects():
    """Handles any request to the 'projects' url."""
    return render_template("projects.html")


@project_bp.route('/account')
@login_required
def account():
    """Handles any request to the 'account' secondary nav-bar link."""
    return render_template("account.html", user=current_user)


@project_bp.route('/dashboards')
@login_required
def dashboards():
    """Handles any request to the 'dashboards' secondary nav-bar link."""
    return render_template("dashboards.html")


@project_bp.route('/monitors')
@login_required
def monitors():
    """Handles any request to the 'monitors' secondary nav-bar link."""
    return render_template("monitors.html")


@project_bp.route('/alerts')
@login_required
def alerts():
    """Handles any request to the 'alerts' secondary nav-bar link."""
    return render_template("alerts.html")


@project_bp.route('/theme')
@login_required
def theme():
    """Handles any request to the 'theme' secondary nav-bar link."""
    return render_template("theme.html")


@project_bp.route('/help')
@login_required
def help():
    """Handles any request to the 'help' secondary nav-bar link."""
    return render_template("help.html")


@project_bp.route('/recent')
@login_required
def recent():
    """Handles any request to the 'recent' secondary nav-bar link."""
    return render_template("recent.html")


@project_bp.route('/create')
@login_required
def create():
    """Handles any request to the 'create' secondary nav-bar link."""
    return render_template("create.html")
