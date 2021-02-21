
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object("config.Config")

    db.init_app(app)
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
        db.create_all(checkfirst=True)

        return app
