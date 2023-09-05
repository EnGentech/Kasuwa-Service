#!/usr/bin/python3
from flask import Flask, url_for


app = Flask(__name__)
app.route('/')
def index():
    return "index"


app.route('/login')
def login():
    return "login"


app.route('/user/<username>')
def user(username):
    return f"{username}\'s profile"


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('login'))
        print(url_for('login', next='/'))
        print(url_for('profile', username='Maskoli Favour'))
    app.run(port = '0.0.0.0', host = '5000')
