"""
===========================================================
School Management System Pro
Routes
===========================================================

Purpose:
    Contains all application routes.

Author:
    Muhammad Rafique
===========================================================
"""

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from app.extensions import db

from app.models import (
    User,
    Student
)

from app.forms import (
    LoginForm,
    RegistrationForm,
    StudentForm
)

main = Blueprint(
    "main",
    __name__
)


# ==========================================================
# Home
# ==========================================================

@main.route("/")
def home():

    return render_template(
        "index.html"
    )


# ==========================================================
# Dashboard
# ==========================================================

@main.route("/dashboard")
@login_required
def dashboard():

    total_students = Student.query.count()

    return render_template(
        "dashboard.html",
        total_students=total_students
    )


# ==========================================================
# Register
# ==========================================================

@main.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if current_user.is_authenticated:

        return redirect(
            url_for("main.dashboard")
        )

    form = RegistrationForm()

    if form.validate_on_submit():

        existing_user = User.query.filter_by(
            email=form.email.data.lower()
        ).first()

        if existing_user:

            flash(
                "Email already registered.",
                "danger"
            )

            return redirect(
                url_for("main.register")
            )

        user = User(

            username=form.username.data,

            email=form.email.data.lower(),

            role="admin"

        )

        user.set_password(
            form.password.data
        )

        db.session.add(user)

        db.session.commit()

        flash(

            "Registration Successful. Please Login.",

            "success"

        )

        return redirect(
            url_for("main.login")
        )

    return render_template(

        "register.html",

        form=form

    )


# ==========================================================
# Login
# ==========================================================

@main.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if current_user.is_authenticated:

        return redirect(
            url_for("main.dashboard")
        )

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(

            email=form.email.data.lower()

        ).first()

        if user and user.check_password(

            form.password.data

        ):

            login_user(user)

            flash(

                "Welcome Back!",

                "success"

            )

            return redirect(

                url_for("main.dashboard")

            )

        flash(

            "Invalid Email or Password.",

            "danger"

        )

    return render_template(

        "login.html",

        form=form

    )


# ==========================================================
# Logout
# ==========================================================

@main.route("/logout")
@login_required
def logout():

    logout_user()

    flash(

        "Logged Out Successfully.",

        "info"

    )

    return redirect(

        url_for("main.login")

    )
# ==========================================================
# Student List
# ==========================================================

@main.route("/students")
@login_required
def students():

    students = Student.query.order_by(
        Student.created_at.desc()
    ).all()

    return render_template(
        "students.html",
        students=students
    )
# ==========================================================
# Add Student
# ==========================================================

@main.route("/add_student", methods=["GET", "POST"])
@login_required
def add_student():

    form = StudentForm()

    if form.validate_on_submit():

        existing_student = Student.query.filter_by(
            email=form.email.data.lower()
        ).first()

        if existing_student:

            flash(
                "A student with this email already exists.",
                "danger"
            )

            return render_template(
                "add_student.html",
                form=form
            )

        student = Student(

            name=form.name.data.strip(),

            age=form.age.data,

            email=form.email.data.lower(),

            phone=form.phone.data,

            gender=form.gender.data,

            address=form.address.data,

            course=form.course.data

        )

        db.session.add(student)

        db.session.commit()

        flash(
            "Student added successfully!",
            "success"
        )

        return redirect(
            url_for("main.students")
        )

    return render_template(
        "add_student.html",
        form=form
    )
# ==========================================================
# Student Details
# ==========================================================

@main.route("/student/<int:id>")
@login_required
def student_detail(id):

    student = Student.query.get_or_404(id)

    return render_template(
        "student_detail.html",
        student=student
    )
# ==========================================================
# Edit Student
# ==========================================================

@main.route(
    "/edit_student/<int:id>",
    methods=["GET", "POST"]
)
@login_required
def edit_student(id):

    student = Student.query.get_or_404(id)

    form = StudentForm(obj=student)

    if form.validate_on_submit():

        student.name = form.name.data.strip()

        student.age = form.age.data

        student.email = form.email.data.lower()

        student.phone = form.phone.data

        student.gender = form.gender.data

        student.address = form.address.data

        student.course = form.course.data

        db.session.commit()

        flash(
            "Student updated successfully!",
            "success"
        )

        return redirect(
            url_for("main.students")
        )

    return render_template(
        "edit_student.html",
        form=form,
        student=student
    )
# ==========================================================
# Delete Student
# ==========================================================

@main.route("/delete_student/<int:id>")
@login_required
def delete_student(id):

    student = Student.query.get_or_404(id)

    db.session.delete(student)

    db.session.commit()

    flash(
        "Student deleted successfully!",
        "warning"
    )

    return redirect(
        url_for("main.students")
    )