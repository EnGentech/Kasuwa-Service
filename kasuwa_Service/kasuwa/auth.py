from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from .Base_connect import session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form
    # print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = session.query(User).filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successful', category='success')
                login_user(user, remember=True)
                return redirect(url_for('Views.index'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    # data = request.form
    # print(data)
    # Initialize success_msg with an empty string

    if request.method == "POST":
        name = request.form.get('name')
        password1 = request.form.get('password')
        password2 = request.form.get('password')
        email = request.form.get('email')
        phone = request.form.get('phone')


        existing_usr = session.query(User).filter_by(email=email).first()
        if existing_usr:
            flash("User already exists, Please login", "error")
            return redirect(url_for("auth.login"))
        if len(name) < 2:
           flash("name must be greater than 1 character.", category="error")
           return redirect(url_for("auth.signup"))
        elif password1 != password2:
            flash("passwords don't match.", category="error")
            return redirect(url_for("auth.signup"))
        elif len(password1) < 7:
            flash("password must be greater than or equal to 7 characters.", category="error")
            return redirect(url_for("auth.signup"))
        elif len(email) < 4:
            flash("email is too short.", category="error")
            return redirect(url_for("auth.signup"))
        elif len(phone) < 5:
            flash("phone is not valid.", category="error")
            return redirect(url_for("auth.signup"))
        else:
            # add user
            user = User(
            username=name, 
            fullname=name, 
            email=email,
            password=generate_password_hash(password1, method='sha256'),
            address='address',
            phone=phone,
            # gender=default, 
            # birthDate = datetime.strptime('2000-01-01', '%Y-%m-%d').date()
            )
            session.add(user)
            session.commit()
            login_user(user, remember=True)
            flash("Account created successfully!", category="success")
            return redirect(url_for('Views.index'))

    return render_template("sign_up.html")

@auth.route('/shopping_cart', methods=['GET', 'POST'])
@login_required
def shopping_cart():
    data = request.form
    print(data)

    # if request.method=='POST':
    return render_template('shopping_cart.html')

@auth.route('/my_orders', methods=['GET', 'POST'])
@login_required
def my_orders():
    return render_template('my_orders.html')

@auth.route('/my_coins', methods=['GET', 'POST'])
@login_required
def my_coins():
    return render_template('my_coins.html')

@auth.route('/message_center', methods=['GET', 'POST'])
@login_required
def message_center():
    return render_template('message_center.html')

@auth.route('/payment', methods=['GET', 'POST'])
@login_required
def payment():
    return render_template('payment.html')

@auth.route('/wish_list', methods=['GET', 'POST'])
@login_required
def wish_list():
    return render_template('wish_list.html')

@auth.route('/my_favourite_stores', methods=['GET', 'POST'])
@login_required
def my_fav_stores():
    return render_template('my_fav_stores.html')

@auth.route('/my_coupons', methods=['GET', 'POST'])
@login_required
def my_coupons():
    return render_template('my_coupons.html')