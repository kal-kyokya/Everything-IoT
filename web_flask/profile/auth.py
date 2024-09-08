#!/usr/bin/python3
"""
'auth' contains the routes required during user authentication.
"""
# Import the necessary modules and/or tools
from flask import (
    Blueprint, flash, render_template,
    redirect, request, url_for)
from flask_login import login_user, login_required, logout_user, current_user
from models.user import User
from models.dashboard import Dashboard
from models.microcontroller import Microcontroller
from models.sensor import Sensor
from models.type import Type
from models.thing import Thing
from models.location import Location
from models import storage
from werkzeug.security import check_password_hash


# Declare this file as Blueprint to the Everything IoT Web App
auth_bp = Blueprint('auth', __name__)


# Define the routes associated with authentication and their handler functions
@auth_bp.route('/sign-up', methods=['GET', 'POST'])
def signup():
    """Backend logic to be implemented upon new user registration attempt."""
    if request.method == 'POST':
        # Get user details
        form = request.form
        MUST_HAVE = ['firstname', 'lastname', 'email',
                     'username', 'password', 'password1']

        # Ensure the required fields are provided
        MISSING = []
        for field in MUST_HAVE:
            if field not in form.keys() or form.get(field) == "":
                MISSING.append(field.capitalize())
        if len(MISSING) > 0:
            flash("{} must be filled".format(MISSING),
                  category='missing_input')
            return redirect(url_for('auth.signup'))

        # Ensure email not 'already in use'
        # Query User table in database for record whose email match
        # If present flash error message else proceed.
        users = storage.all(User)
        if len(users) > 0:
            for user in users.values():
                if user.email == form.get('email'):
                    flash("Email already in use.", category='invalid_input')
                    return redirect('/sign-up')
                elif user.username == form.get('username'):
                    flash("Username already in use.", category='invalid_input')
                    return redirect('/sign-up')

        # Validate each of them and flash error message if invalid
        if len(form.get('email')) < 12:
            flash('The email must be at least 12 characters long.',
                  category='invalid_input')
        elif len(form.get('firstname')) < 2:
            flash('The first name must be at least 2 characters long.',
                  category='invalid_input')
        elif len(form.get('lastname')) < 2:
            flash('The last name must be at least 2 characters long.',
                  category='invalid_input')
        elif form.get('phone') != "" and len(form.get('phone')) < 10:
            flash('The phone number must be at least 12 characters long.',
                  category='invalid_input')
        elif len(form.get('password')) < 8:
            flash('The password must be at least 8 characters long.',
                  category='invalid_input')
        elif form.get('password') != form.get('password1'):
            flash('The passwords do not match.',
                  category='invalid_input')
        else:
            # Create new user
            user_dict = {}
            for key, value in form.items():
                if key == "birthday" and value == "":
                    value = None
                user_dict[key] = value
            new_user = User(**user_dict)
            storage.add(new_user)
            storage.commit()
            login_user(new_user, remember=True)
            flash("Hello {}, welcome to Everything IoT".format(
                form.get('username')), category='success')
            # Redirect to 'logged in' landing page.
            return redirect(url_for('auth.signin'))

    return render_template('signup.html')


@auth_bp.route('/sign-in', methods=['GET', 'POST'])
def signin():
    """Allows users to access their accounts."""
    if request.method == 'POST':
        # Retrieve User credentials
        form = request.form
        userID = form.get('userIdentifier')
        password = form.get('password')

        # Ensure requested user exists in the database
        users = storage.all(User)
        for user in users.values():
            if user.email == userID or user.username == userID:
                # Ensure input password matches the database version
                if check_password_hash(user.password, password):
                    login_user(user, remember=True)
                    return redirect(url_for('home.loggedIn'))
                else:
                    flash("Invalid password", category='invalid_input')
                    break

        flash("Check Username/Email or Sign Up", category='invalid_input')
        return render_template('signin.html')

    else:
        return render_template('signin.html')

@auth_bp.route('/logout')
@login_required
def logout():
    """Handles user logout requests."""
    # End session
    logout_user()
    # Redirect to the 'logged out' page
    return redirect(url_for('home.home'))
