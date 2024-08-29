#!/usr/bin/python3
"""
'auth' contains the routes required during user authentication.
"""
# Import the necessary modules and/or tools
from flask import Blueprint, flash, render_template, request


# Declare this file as Blueprint to the Everything IoT Web App
auth_bp = Blueprint('auth', __name__)


# Define the routes associated with authentication and their handler functions
@auth_bp.route('/sign-up', methods=['GET', 'POST'])
def signup():
    """Backend logic to be implemented upon new user registration attempt."""
    if request.method == 'POST':
        # Get user details
        form = request.form
        must_have = ['email', 'firstName', 'lastName',
                     'birthday', 'password1', 'password2']

        # Ensure email not 'already in use'
        # Query User table in database for record whose email match
        # If present flash error message else proceed.

        # Ensure some required fields are provided
        for key in form.keys():
            if key not in must_have:
                print("missing {} input".format(key))
                flash("{} must be filled".format(key),
                      category='missing_input')

        # Validate each of them and flash error message if invalid
        if len(form.get('email')) < 12:
            flash('The email must be at least 12 characters long.',
                  category='invalid_input')
        elif len(form.get('firstName')) < 2:
            flash('The first name must be at least 2 characters long.',
                  category='invalid_input')
        elif len(form.get('lastName')) < 2:
            flash('The last name must be at least 2 characters long.',
                  category='invalid_input')
        elif len(form.get('phoneNumber')) != 12:
            flash('The phone number must be at least 12 characters long.',
                  category='invalid_input')
        elif len(form.get('password1')) < 8:
            flash('The password must be at least 8 characters long.',
                  category='invalid_input')
        elif form.get('password1') != form.get('password2'):
            flash('The two password do not match.',
                  category='invalid_input')
        else:
            flash("Hello {}, welcome to Everything IoT".format(
                form.get('username')), category='success')
            return redirect(url_for(home.routes.home))

        # Redirect to 'logged in' landing page.

    return render_template('signup.html')


@auth_bp.route('/sign-in', methods=['GET', 'POST'])
def signin():
    """Allows users to access their accounts."""
    # Retrieve User credentials
    form = request.form
    user = form.get('userIdentifier')
    pwd = form.get('password')

    """    # Ensure requested user exists in the database
    email = query.User.filter_by(email=user).first()
    username = query.User.filter_by(username=user).first()

    if email or username:
        query_obj = query.User.filter_by(password=pwd).first()
        # Ensure input password matches the database version
        if query_obj and user == query_obj.get('email') or
        user == query_obj.get('username'):
            return redirect(url_for(home.routes.home))"""
    return render_template('signin.html')


@auth_bp.route('/logout')
def logout():
    """Handles user logout requests."""
    # Ensure there was an ongoing user session

    # End session

    # Redirect to 'logged out' landing page
    return render_template('home.html')
