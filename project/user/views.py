# project/place/views.py

# imports
from flask import Blueprint, render_template

# config
user_blueprint = Blueprint("user", __name__, template_folder="templates/user")

# routes
@user_blueprint.route('/login')
def index():
    return render_template("login.html")
