"""Database models. """

import sys
import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func
from . import db


class User(UserMixin, db.Model):

    __tablename__ = "flask-users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=False)
    username = db.String(20)
    email = db.Column(db.String(40), primary_key=False, unique=False, nullable=False)
    password = db.Column(
        db.String(200), primary_key=False, unique=False, nullable=False
    )

    def set_password(self, password):
        self.password = generate_password_hash(password, method="sha256")

    def check_password_hash(self, password):
        print(self.password, file=sys.stderr)
        return check_password_hash(self.password, password)

    def get_password(self):
        return self.password

    def __repr__(self):
        return "<User {}>".format(self.name)


class Post(db.Model):

    __tablename__ = "blog-post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=False)
    author_id = db.Column(db.ForeignKey("flask-users.id"))
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return "<Post {}>".format(self.title)
