"""
===========================================================
School Management System Pro
Database Models
===========================================================

Author:
    Muhammad Rafique

Purpose:
    Contains all database models used in the application.
===========================================================
"""

from datetime import datetime

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from flask_login import UserMixin

from app.extensions import db


# ===========================================================
# User Model
# ===========================================================

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(20),
        nullable=False,
        default="student"
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # One user -> one student profile
    student = db.relationship(
        "Student",
        back_populates="user",
        uselist=False
    )

    # ---------------------------------------

    def set_password(self, password):

        self.password_hash = generate_password_hash(
            password
        )

    # ---------------------------------------

    def check_password(self, password):

        return check_password_hash(
            self.password_hash,
            password
        )

    # ---------------------------------------

    def __repr__(self):

        return f"<User {self.username}>"


# ===========================================================
# Student Model
# ===========================================================

class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    age = db.Column(
        db.Integer,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    phone = db.Column(
        db.String(20)
    )

    gender = db.Column(
        db.String(20)
    )

    address = db.Column(
        db.Text
    )

    course = db.Column(
        db.String(100)
    )

    image = db.Column(
        db.String(255),
        default="default.png"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    user = db.relationship(
        "User",
        back_populates="student"
    )

    def __repr__(self):

        return f"<Student {self.name}>"