import sys
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from auth import db


class User(UserMixin, db.Model):

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=False)
    username = db.String(20)
    email = db.Column(
        db.String(40),
        primary_key=False,
        unique=False,
        nullable=False)
    password = db.Column(
        db.String(200), primary_key=False, unique=False, nullable=False
    )
    posts = db.relationship("Post", backref="author")

    def set_password(self, password):
        self.password = generate_password_hash(password, method="sha256")

    def check_password_hash(self, password):
        return check_password_hash(self.password, password)

    def get_password(self):
        return self.password

    def __repr__(self):
        return "<User {}>".format(self.name)
