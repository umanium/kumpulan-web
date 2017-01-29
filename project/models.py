from project import db


class Place(db.Model):

    __tablename__ = "places"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __init__(self, name, description, latitude=None, longitude=None):
        self.name = name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "place %s" % (self.name)
