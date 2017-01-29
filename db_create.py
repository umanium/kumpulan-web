from project import db
from project.models import Place


# create the database
db.create_all()

# insert place data
place1 = Place("Kantor pemkot", "Kantor pemerintah Kota Cimahi", -6.8736073, 107.5564327)
place2 = Place("Kolam renang Ciawitali", "Kolam renang Ciawitali")
place3 = Place("SMAN 15 Bandung", "SMA Negeri 15 Bandung", -6.8736073, 107.5564327)
db.session.add(place1)
db.session.add(place2)
db.session.add(place3)

# commit the changes
db.session.commit()
