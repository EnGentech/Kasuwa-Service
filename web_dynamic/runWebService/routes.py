import sys
sys.path.append(r"c:\Users\Engr. Gentle Inyang\Web_Application_Projects\Kasuwa-Service\web_dynamic")
import database_management

from flask import Blueprint, render_template, request, url_for, redirect, session, flash
from functools import wraps
from mailVerification import send_verification_email
from database_management import Db_Management
from flask_bcrypt import Bcrypt
from random import randint
from datetime import datetime

start = Blueprint('kasu', __name__, template_folder='templates')

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'e_mail' not in session:
            pwdUrl(request.url)
            return redirect(url_for('kasu.sign_in'))
        return func(*args, **kwargs)
    return decorated_function

@start.route('/', methods=['GET'])
@start.route('/kasuwa', methods=["GET"])
def main():
    """render the index page"""
    category = Db_Management().category()
    if category:
        if request.method == 'GET':
            sendid = randint(1, len(category) + 1)
            displayProducts = Db_Management().product_category(2)
            return render_template('index.html', category=category, productsIndex=displayProducts)
    else:
        return render_template('index.html', category='No category, check back')

@start.route('/kasuwa/index/category/product', methods=['GET', 'POST'])
def product():
    """display product from category"""
    category = Db_Management().category()
    if category:
        if request.method == 'GET':
            return render_template('category_page.html')
        elif request.method == "POST":
            cat_id = request.form.get('cat_id')
            catName = request.form.get('cat_name')
            new_id = cat_id.split('d')
            id = int(new_id[1])
            products = Db_Management().product_category(id)
            return render_template('category_page.html', products=products, cat_name=catName)
    else:
        return render_template('index.html', category='No category, check back')

@start.route('/kasuwa/sign_in', methods=['GET', 'POST'])
def sign_in():
    """Write sign in code"""
    category = Db_Management().category()
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
                return render_template('index.html', userS=userS[0], category=category)

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
            

@start.route('/kasuwa/cart', methods=['GET', 'POST'])
def cart():
    """store the current url and redirect to login"""
    cart = session.get('cart', [])
    if request.method == 'GET':
        @login_required
        def cart_get(): 
            increase = 0 
            lis = []
            if session['e_mail']:
                email = (session['e_mail'])
                userid = Db_Management().get_active_userID(email)
                retriveProducts = Db_Management().cartProductIDs(userid[0])
            if len(cart) == 0 and len(retriveProducts) == 0:
                return render_template('shoping_cart.html', count=0)
            else:
                cart_list = retriveProducts
                increase = len(retriveProducts)
                if len(cart) > 0:
                    for pid in cart:
                        increase += 1
                        catid = Db_Management().get_catID(pid['pid'])
                        qty = pid['qty']
                        #Db_Management().addToCart(pid['pid'], catid[0], userid[0], qty)
                    newlist = Db_Management().cartProductIDs(userid[0])
                    for content in newlist:
                        gotten = Db_Management().view_product(content[0])
                        lis.append(gotten)
                else:
                    for content in cart_list:
                        gotten = Db_Management().view_product(content[0])
                        lis.append(gotten)                    
                     
            return render_template('shoping_cart.html', lis=lis, count=increase)
        return cart_get()
        
    elif request.method == 'POST':
        pid = request.form.get('productid')
        qty = request.form.get('quantity')
        
        cartSelect = {'pid':pid, 'qty':qty}

        cart.append(cartSelect)
        session['cart'] = cart
        return 'Successful'

@start.route('/kasuwa/signOut')
@login_required
def signOut():
    """Sign out route create if there exist a login session"""
    session.pop('e_mail', None)
    session.pop('cart', None)
    return redirect(url_for('kasu.main'))


@start.route('/kasuwa/category/products', methods=['GET', 'POST'])
def products():
    """render the products to users"""
    time = datetime.now()
    time = time.strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "GET":
        return render_template('product.html')
    elif request.method == 'POST':
        productID = request.form.get('prodID')
        renderCart = Db_Management().view_product(productID)
        print(renderCart)
        return render_template('product.html', productInView=renderCart, time=time)

def pwdUrl(url):
    """store present user URL"""
    session['store'] = url
