# Modelo da categoria usuário
from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name_complete = db.Column(db.String(100), unique=False, nullable=False)
    nameuser = db.Column(db.String(35), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    senha = db.Column(db.String(35), nullable=False)