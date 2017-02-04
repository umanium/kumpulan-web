# project/place/views.py

# imports
from flask import render_template, Blueprint
from project.models import Place

# config
place_blueprint = Blueprint("place", __name__, template_folder="templates/place", url_prefix="/places")

# routes
@place_blueprint.route('/')
def index():
    all_places = Place.query.all()
    return render_template("index.html", all_places=all_places)
