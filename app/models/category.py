# Modelo para criação das categórias
from app import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    color = db.Column(db.String(30))