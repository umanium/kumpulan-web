# project/place/views.py

# imports
from flask import render_template, Blueprint

# config
place_blueprint = Blueprint("place", __name__, template_folder="templates/place", url_prefix="/places")

# routes
@place_blueprint.route('/')
def index():
    return render_template("index.html")
