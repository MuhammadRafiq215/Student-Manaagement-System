"""
===========================================================
School Management System Pro
Forms
===========================================================

Author:
    Muhammad Rafique
===========================================================
"""

from flask_wtf import FlaskForm

from flask_wtf.file import (
    FileField,
    FileAllowed
)

from wtforms import (
    StringField,
    PasswordField,
    IntegerField,
    SubmitField,
    TextAreaField,
    SelectField
)

from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    NumberRange,
    Optional
)


# ===========================================================
# Login Form
# ===========================================================

class LoginForm(FlaskForm):

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField(
        "Login"
    )


# ===========================================================
# Registration Form
# ===========================================================

class RegistrationForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=3, max=50)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo(
                "password",
                message="Passwords must match."
            )
        ]
    )

    submit = SubmitField(
        "Register"
    )


# ===========================================================
# Student Form
# ===========================================================

class StudentForm(FlaskForm):

    name = StringField(
        "Full Name",
        validators=[
            DataRequired()
        ]
    )

    age = IntegerField(
        "Age",
        validators=[
            DataRequired(),
            NumberRange(min=3, max=100)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    phone = StringField(
        "Phone",
        validators=[
            Optional()
        ]
    )

    gender = SelectField(
        "Gender",
        choices=[
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other")
        ]
    )

    address = TextAreaField(
        "Address",
        validators=[
            Optional()
        ]
    )

    course = StringField(
        "Course",
        validators=[
            Optional()
        ]
    )

    image = FileField(
        "Profile Picture",
        validators=[
            FileAllowed(
                ["jpg", "jpeg", "png"],
                "Images only!"
            )
        ]
    )

    submit = SubmitField(
        "Save Student"
    )