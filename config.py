"""
===========================================================
School Management System
Configuration
===========================================================

Purpose:
    Stores all configuration settings for the application.

Author:
    Muhammad Rafique
===========================================================
"""

import os


class Config:

    # Secret Key
    SECRET_KEY = "StudentManagementSystem2026"

    # Project Base Directory
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # SQLite Database
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        BASE_DIR,
        "instance",
        "student_management.db"
    )

    # Disable Modification Tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload Folder
    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "app",
        "static",
        "uploads"
    )

    # Maximum Upload Size (5 MB)
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024