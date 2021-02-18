"""Database models. """

import sys
import datetime
from blog import db
from sqlalchemy.sql import func


class Post(db.Model):

    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    time_created = db.Column(
        db.DateTime(
            timezone=True),
        server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return "<Post {}>".format(self.title)
