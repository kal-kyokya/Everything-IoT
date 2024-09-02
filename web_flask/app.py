#!/usr/bin/python3
"""
'app' contains the callable to be used as Web Application for Everything IoT.
"""
# From the required modules import the associated tools
from flask import Flask
from home.routes import home_bp
from profile.auth import auth_bp


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


# Only run the web app if this file directly executed,
# not if it is imported as a module in another script.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
