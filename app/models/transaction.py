# Modelo da categoria trasnsação
from app import db


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text)
    id_category = db.Column(db.Integer, db.ForeignKey('category.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))