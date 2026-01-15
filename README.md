# OCS-Problem-Statement — Flask demo app
A small Flask web application demonstrating a simple login flow backed by a SQLAlchemy user model. If a user authenticates and has role admin, they see all users; otherwise they see only their own record. The site is currently not in deployment.

Features
Flask web app with a single route / (GET shows login form, POST attempts authentication).
SQLAlchemy user model (fields: userid (PK), password_hash, role).
Simple password hashing helper using MD5 (hashing.hashof()).
Minimal Jinja2 templates:
home.html — login form
table.html — table display of users
Run with python run.py (development mode; debug enabled in run.py).
Requirements
Python 3.10+ recommended
The project dependencies are listed in requirements.txt. Install via pip.
Quickstart (development)
Clone the repository and change into it:

git clone https://github.com/your-username/OCS-Problem-Statement.git
cd OCS-Problem-Statement
Create and activate a virtual environment:

macOS / Linux:
python3 -m venv venv
source venv/bin/activate
Windows (PowerShell):
python -m venv venv
venv\Scripts\Activate.ps1
Install dependencies:

pip install -r requirements.txt

By default this repo hard-codes the DB URI in app_main.py. Replace that with an environment-variable-based setting before running.
Example (Linux/macOS):
export DATABASE_URL="postgresql://username:password@host:port/dbname"
Windows (PowerShell):
$env:DATABASE_URL="postgresql://username:password@host:port/dbname"
Update app_main.py to read the environment variable (example snippet below under "Configuration").
Run the app (development):

python run.py
The app will be available at http://127.0.0.1:5000/ (or 0.0.0.0:5000 if run from a server) (localhost, not deployed this site).

Configuration
Recommended change to app_main.py to avoid hard-coded credentials and allow local fallback (example):

# app_main.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',
        'sqlite:///dev.db'  # local fallback for quick testing
    )
    db.init_app(app)
    from routes import all_routes
    all_routes(app, db)
    return app
Set DATABASE_URL in your environment to your Postgres connection string when running in production.

Database setup & creating a user
You can create tables and add an initial user (useful for testing) with this short script. Replace admin, password123, and role as needed.

Create a file create_user.py in the project root:

# create_user.py
from app_main import create_app, db
from conn_db import user
from hashing import hashof

app = create_app()

with app.app_context():
    # Create tables (runs CREATE TABLE if missing)
    db.create_all()

    # Create an admin user
    u = user(userid='admin', password_hash=hashof('password123'), role='admin')
    db.session.add(u)
    db.session.commit()
    print("Created user:", u)
Run it:

python create_user.py

Using the app
Open your browser to: http://127.0.0.1:5000/
Enter the username and password you created (example above: username admin, password password123).
If the user exists and the MD5 hash matches, the app renders table.html.
If user's role is admin, the table lists all users.
Otherwise it lists only the authenticated user's row.
Example using curl to POST credentials:

curl -X POST -F "username=admin" -F "password=password123" http://127.0.0.1:5000/
If login fails, the app returns the login page again (no explicit error message).

Project structure
run.py — simple entrypoint that creates the app and runs Flask.
app_main.py — app factory and SQLAlchemy initialization (currently contains DB URI — see Configuration).
routes.py — defines all_routes(app, db) and the / route (login + table rendering).
conn_db.py — SQLAlchemy model for user.
hashing.py — small helper using MD5: hashof(s).
templates/
base.html — base template
home.html — login form
table.html — user table view
requirements.txt — dependency list
Security & hardening (important)
