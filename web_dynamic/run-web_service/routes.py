from flask import Blueprint, render_template, request, url_for, redirect, session
from functools import wraps
import database_management

start = Blueprint('main_bp', __name__, template_folder='templates')

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'userName' not in session:
            return redirect(url_for('redirect_me'))
        return func(*args, **kwargs)
    return decorated_function

@start.route('/kasuwa/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        e_mail = request.form.get('mail')
        phoneNumber = request.form.get('phoneNumber')
        reg = [username, password, e_mail, phoneNumber]
        Db_Management.new_user(reg)

@start.route('/')
def index():
    return render_template('basic.html')

@start.route('/kasuwa/index')
def main():
    return render_template('index.html')

@start.route('/cart')
def cart():
    return render_template('shoping_cart.html')


import sys
print(sys.path)