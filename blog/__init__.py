import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        from . import routes
        from . import auth
        #from .assets import compile_assets

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(commands.usersbp)
        # Create Database Models
        db.create_all()

        # Compile static assets
        #if app.config['FLASK_ENV'] == 'development':
        #    compile_assets(app)

        return app

from .commands import usersbp
