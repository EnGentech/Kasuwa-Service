from flask import Flask
from flask_mail import Mail
from routes import start

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(start)
    
    return app
