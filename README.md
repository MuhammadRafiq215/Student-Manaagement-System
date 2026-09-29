# School Management System Pro

A role-based school management platform built with Flask. Each role (Admin,
Teacher, Student) gets its own dashboard and features. The project is web-first
and structured so it can later be packaged as a mobile app.

## Features
- Secure login with role-based access (Admin / Teacher / Student)
- Admin: manage users, classes, subjects, announcements
- Teacher: take attendance, enter grades, post assignments
- Student: view timetable, attendance, grades, announcements
- Database migrations with Flask-Migrate

## Tech Stack
Python, Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF, Flask-Migrate, SQLite

## Getting Started
    git clone https://github.com/<your-username>/<repo-name>.git
    cd <repo-name>
    python -m venv .venv
    .venv\Scripts\activate          # Windows
    pip install -r requirements.txt
    copy .env.example .env          # then edit SECRET_KEY
    flask db upgrade                # or: python create_db.py
    python run.py

Open http://127.0.0.1:5000

## Roadmap
- [ ] Parent role
- [ ] REST API (/api/v1) for the mobile app
- [ ] Installable PWA
- [ ] Reports and PDF export

## Author
Muhammad Rafique
