import sys
sys.path.append(r"c:\Users\Engr. Gentle Inyang\Web_Application_Projects\Kasuwa-Service\web_dynamic")
import database_management

from flask import Blueprint, render_template, request, url_for, redirect, session, flash
from functools import wraps
from mailVerification import send_verification_email
from database_management import Db_Management
from flask_bcrypt import Bcrypt

start = Blueprint('kasu', __name__, template_folder='templates')

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'e_mail' not in session:
            pwdUrl(request.url)
            return redirect(url_for('kasu.sign_in'))
        return func(*args, **kwargs)
    return decorated_function

@start.route('/')
@start.route('/kasuwa')
def main():
    return render_template('index.html')

@start.route('/kasuwa/sign_in', methods=['GET', 'POST'])
def sign_in():
    """Write sign in code"""
    if request.method == 'GET':
        return render_template('sign_in.html')
    elif request.method == "POST":
        e_mail = request.form.get('mail')
        password = request.form.get('password')
        validate = Db_Management().authenticate(e_mail, password)
        if validate == "invalid_credentials":
            return render_template('sign_in.html', error="Invalid credentials, please sign_up")
        elif validate == "invalid_email":
            return render_template('sign_in.html', error="e_mail not found, use the sign up option")
        elif validate == 'invalid_password':
            return render_template('sign_in.html', error="Incorrect password")
        else:
            session['e_mail'] = e_mail
            userS = Db_Management().get_active_user(e_mail)
            stored_url = session.pop('store', None)
            if stored_url:
                #render_template('', userS=userS[0])
                return redirect(stored_url)
            else:
                return render_template('index.html', userS=userS[0])

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
            flash('Sign Up was successful, please sign_in')
            return render_template('sign_in.html')
            

@start.route('/kasuwa/cart')
@login_required
def cart():
    """store the current url and redirect to login"""
    return render_template('shoping_cart.html')

@start.route('/kasuwa/signOut')
@login_required
def signOut():
    """Sign out route create if there exist a login session"""
    session.pop('e_mail', None)
    return redirect(url_for('kasu.main'))

def pwdUrl(url):
    """store present user URL"""
    session['store'] = url
