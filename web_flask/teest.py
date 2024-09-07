#!/usr/bin/python3
"""
'app' contains the callable to be used as Web Application for Everything IoT.
"""
# From the required modules import the associated tools
from flask import Flask
from flask_login import LoginManager
from home.routes import home_bp
from models import storage
from profile.auth import auth_bp
from projects.work import project_bp


# Make this file the web app controller
app = Flask(__name__)

# Initialize web app's sercret key
with open('secret_key', 'r') as skey:
    key = skey.read()
    app.config['SECRET_KEY'] = key

# Make Flask provide detailed error pages and
# automatically reload server when code changes.
app.config['DEBUG'] = True

# Disable strictness on slashes for all defined routes.
app.url_map.strict_slashes = False

# Register associated Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(project_bp)

# Initialize a utility that tracks any logged in user
login_manager = LoginManager()
# Bind the utility to the web app
login_manager.init_app(app)
# Define the default route
login_manager.login_view = "auth.signin"

# Define method that fetches logged in user's object format
@login_manager.user_loader
def load_user(user_id):
    """Retrieve a user based on its ID.
    Arg:
        user_id: The unique identifier of the user."""
    users = storage.all().values()
    for user in users:
        if user.id == user_id:
            return user

# Only run the web app if this file's directly executed,
# not if it is imported as a module in another script.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
