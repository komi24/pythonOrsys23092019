from . import db


class Personne(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String())
    prenom = db.Column(db.String())
    age = db.Column(db.Integer)
    pic = db.Column(db.String())
