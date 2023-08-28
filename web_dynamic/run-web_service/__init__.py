from flask import Flask
from flask_mail import Mail
from routes import start

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(start)

    # Configuration for Flask-Mail and Gmail
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'engen.inyang@gmail.com'
    app.config['MAIL_PASSWORD'] = 'Jesus@Christ8634'

    mail = Mail(app)
    
    return app
