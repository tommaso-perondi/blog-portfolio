import click
from flask import Blueprint
from .models import db, User


usersbp = Blueprint("users", __name__)


@usersbp.cli.command("create")
@click.argument("name")
@click.argument("username")
@click.argument("email")
@click.argument("password")
def create(name, username, email, password):
    """ Creates a user """
    print("Create user: {}".format(name))
    newUser = User(name=name, email=email)
    newUser.set_password(password)
    print(newUser.get_password())
    db.session.add(newUser)
    db.session.commit()
