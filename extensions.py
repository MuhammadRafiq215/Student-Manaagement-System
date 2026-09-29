"""
===========================================================
School Management System Pro
Extensions
===========================================================

Purpose:
    Initializes all Flask extensions.

Author:
    Muhammad Rafique
===========================================================
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# ----------------------------------------------------------
# SQLAlchemy Database
# ----------------------------------------------------------

db = SQLAlchemy()

# ----------------------------------------------------------
# Login Manager
# ----------------------------------------------------------

login_manager = LoginManager()

login_manager.login_view = "main.login"

login_manager.login_message = (
    "Please login first."
)

login_manager.login_message_category = "warning"