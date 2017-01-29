from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

db = SQLAlchemy(app)

# blueprints
from project.place.views import place_blueprint
from project.user.views import user_blueprint

# register the blueprints
app.register_blueprint(place_blueprint)
app.register_blueprint(user_blueprint)
