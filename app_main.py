from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
def create_app():
    app=Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:2024EE10710OCS@db.naqsaosszkjxbywwhcao.supabase.co:5432/postgres'
    db.init_app(app)
    from routes import all_routes
    all_routes(app,db)
    return app