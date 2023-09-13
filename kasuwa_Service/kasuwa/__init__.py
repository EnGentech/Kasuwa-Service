from flask import Flask
from .Base_connect import db_uri, engine, Base, session
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SECRET_KEY'] = 'JHGHGGJJKKKBG'

    

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    Base.metadata.create_all(engine)
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(id):
        return session.query(User).get(int(id))
    

    print("creating table")

    return app
