from flask_login import UserMixin
from genai import db

class User(UserMixin, db.Model):
    """Model for user accounts."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))
    username = db.Column(db.String(32))

    def __str__(self):
        return self.username

    def __repr__(self):
        return '<User {}>'.format(self.username)
