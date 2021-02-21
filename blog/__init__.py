
import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import inspect


import logging
logging.basicConfig(level=logging.DEBUG)

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    db.init_app(app)
    engine = db.get_engine(app)
    inspector = inspect(engine)
    login_manager.init_app(app)
    with app.app_context():
        from blog import routes
        from blog.auth import routes as auth_routes, commands as auth_commands
        from blog.errors.handlers import errors
        # Register Blueprints
        app.register_blueprint(routes.main)
        app.register_blueprint(auth_routes.auth)
        app.register_blueprint(auth_commands.usersbp)
        app.register_blueprint(errors)
        # Create Database Models
        if inspector.get_table_names() == []:
            db.create_all()

        return app
