from flask import Flask
from app_main import create_app

app=create_app()

if __name__=="__main__":
    app.run(debug=True)

