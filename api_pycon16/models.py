from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Puppy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(64), index=True)
    name = db.Column(db.String(64), nullable=False)
    image_url = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, default=1)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    api_key = db.Column(db.String(64), unique=True, index=True)
