from flask import Flask
from .Base_connect import db_uri, engine, Base
from os import path

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SECRET_KEY'] = 'JHGHGGJJKKKBG'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    Base.metadata.create_all(engine)
    print("creating table")


    return app