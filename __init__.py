"""
===========================================================
School Management System Pro
Application Factory
===========================================================

Purpose:
    Creates and configures the Flask application.

Author:
    Muhammad Rafique
===========================================================
"""

from flask import Flask

from app.config import Config
from app.extensions import (
    db,
    login_manager
)


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize Extensions

    db.init_app(app)

    login_manager.init_app(app)

    # -----------------------------------------------
    # Import User AFTER db initialization
    # -----------------------------------------------

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):

        return User.query.get(
            int(user_id)
        )

    # -----------------------------------------------
    # Register Blueprints
    # -----------------------------------------------

    from app.routes import main

    app.register_blueprint(main)

    return app