from flask import Flask
import secrets
from flask_mail import Mail
from routes import start

def create_app():
    app = Flask(__name__)
    
    secret_key = secrets.token_hex(16)
    app.config['SECRET_KEY'] = secret_key
    
    app.register_blueprint(start)
    
    return app
