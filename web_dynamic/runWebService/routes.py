import sys
sys.path.append(r"c:\Users\Engr. Gentle Inyang\Web_Application_Projects\Kasuwa-Service\web_dynamic")
import database_management

from flask import Blueprint, render_template, request, url_for, redirect, session
from functools import wraps
from mailVerification import send_verification_email
from database_management import Db_Management
from flask_bcrypt import Bcrypt

start = Blueprint('kasu', __name__, template_folder='templates')

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'userName' not in session:
            return redirect(url_for('redirect_me'))
        return func(*args, **kwargs)
    return decorated_function

@start.route('/kasuwa/sign_in', methods=['GET', 'POST'])
def sign_in():
    """Write sign in code"""
    if request.method == 'GET':
        return render_template('sign_in.html')

@start.route('/kasuwa/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        e_mail = request.form.get('mail')
        password = request.form.get('password')
        password = Bcrypt().generate_password_hash(password).decode('utf-8')
        phoneNumber = request.form.get('phoneNumber')
        reg = [username, e_mail, password, phoneNumber]
        #send_verification_email(e_mail, '123ab')
        check = Db_Management().verify_mail(e_mail)
        if check == 'found':
            return render_template('sign_up.html', error="e_mail already registered, please use sign_in option")
        else:
            Db_Management().new_user(reg)
            return "Sign_up Successful"

@start.route('/')
def index():
    return render_template('basic.html')

@start.route('/kasuwa')
def main():
    return render_template('index.html')

@start.route('/kasuwa/cart')
def cart():
    return render_template('shoping_cart.html')
