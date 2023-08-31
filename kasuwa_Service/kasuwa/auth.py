from flask import Blueprint, render_template, redirect, url_for, request, flash
from .Base_connect import session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    # data = request.form
    # print(data)
    if request.method == "POST":
        name = request.form.get('name')
        password1 = request.form.get('password')
        password2 = request.form.get('password')
        email = request.form.get('email')
        phone = request.form.get('phone')   
        # add_user(
        #     username=name,
        #     fullname=name,
        #     email=email,
        #     password=generate_password_hash(password1, method='sha256'),
        #     address="",
        #     phone=phone,
        #     gender=""
        # )
        user = User(
        username=name, 
        fullname=name, 
        email=email,
        password=generate_password_hash(password1, method='sha256'),
        address='address',
        phone=phone,
        gender='gender', 
        birthDate = datetime.strptime('2000-01-01', '%Y-%m-%d').date()
        )
        session.add(user)
        session.commit()
        print("Account created successfully!")
        return redirect(url_for('Views.home'))
    else:
        print("user not registered")

    
        # if len(name) < 2:
        #     flash("name must be greater than 1 characters.", category="error")
        # elif password1 != password2:
        #     flash("passwords must don't match.", category="error")
        # elif len(password1) < 7:
        #     flash("passwords must be greater than or equal to 7 characters.", category="error")
        # elif len(email) < 4:
        #     flash("email too short.", category="error")
        # elif len(phone) < 5:
        #     flash("phone not valid.", category="error")
        # else:
        #     flash("account created successfully!.", category="success")
        #     pass
        #     # add user
        
    return render_template("sign_up.html")
