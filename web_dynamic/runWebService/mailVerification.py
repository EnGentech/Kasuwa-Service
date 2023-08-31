from flask_mail import Message, Mail
from flask import Flask

app = Flask(__name__)
mail = Mail(app)

# Configuration for Flask-Mail and Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'engen.inyang@gmail.com'
app.config['MAIL_PASSWORD'] = 'fcaddbzhoaqjxvhnAavggfrt...11111111'


def send_verification_email(to_email, verification_code):
    """Verification mail sent to users"""
    subject = 'Account Verification'
    sender_email = app.config['MAIL_USERNAME']
    recipient_email = to_email

    message_body = f'Your verification code is: {verification_code}'

    msg = Message(subject=subject, sender=sender_email, recipients=[recipient_email])
    msg.body = message_body

    mail.send(msg)
