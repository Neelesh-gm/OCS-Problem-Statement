from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
def create_app():
    app=Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres.naqsaosszkjxbywwhcao:2024EE10710OCS@aws-0-us-west-1.pooler.supabase.com:6543/postgres'
    db.init_app(app)
    from routes import all_routes
    all_routes(app,db)
    return app