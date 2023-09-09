import sys
sys.path.append(r"c:\Users\Engr. Gentle Inyang\Web_Application_Projects\Kasuwa-Service\web_dynamic")
import database_management

from flask import Blueprint, render_template, request, url_for, redirect, session, flash, jsonify
from functools import wraps
from mailVerification import send_verification_email
from database_management import Db_Management
from flask_bcrypt import Bcrypt
from random import randint
from datetime import datetime

start = Blueprint('kasu', __name__, template_folder='templates')
db = Db_Management()

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'e_mail' not in session:
            pwdUrl(request.url)
            return redirect(url_for('kasu.sign_in'))
        return func(*args, **kwargs)
    return decorated_function

@start.route('/', methods=['GET'])
def lan():
    """landing page"""
    return render_template('landing_page.html')

@start.route('/kasuwa', methods=["GET"])
def main():
    """render the index page"""
    category = db.category()
    displayProduct = []
    if category:
        if request.method == 'GET':
            if 'e_mail' not in session:
                try:
                    for x in range (1, 4):
                        sendid = randint(1, len(category))
                        displayProducts = db.product_category(sendid)
                        displayProduct.append(displayProducts)
                    return render_template('index.html', category=category, productsIndex=displayProduct)
                except Exception:
                    return render_template('index.html', category=category)
            else:
                userS = db.get_active_user(session['e_mail'])
                for x in range (1, 4):
                    sendid = randint(1, len(category) + 1)
                    displayProducts = db.product_category(sendid)
                    displayProduct.append(displayProducts)
                return render_template('index.html', category=category, productsIndex=displayProduct, userS=userS[0])
    else:
        return render_template('index.html', category='No category, check back')

@start.route('/kasuwa/index/category/product', methods=['GET', 'POST'])
def product():
    """display product from category"""
    category = db.category()
    if category:
        if request.method == 'GET':
            return render_template('category_page.html')
        elif request.method == "POST":
            cat_id = request.form.get('cat_id')
            catName = request.form.get('cat_name')
            new_id = cat_id.split('d')
            id = int(new_id[1])
            products = db.product_category(id)
            return render_template('category_page.html', products=products, cat_name=catName)
    else:
        return render_template('index.html', category='No category, check back')

@start.route('/kasuwa/sign_in', methods=['GET', 'POST'])
def sign_in():
    """Write sign in code"""
    category = db.category()
    if request.method == 'GET':
        return render_template('sign_in.html')
    elif request.method == "POST":
        e_mail = request.form.get('mail')
        password = request.form.get('password')
        validate = db.authenticate(e_mail, password)
        if validate == "invalid_credentials":
            return render_template('sign_in.html', error="Invalid credentials, please sign_up")
        elif validate == "invalid_email":
            return render_template('sign_in.html', error="e_mail not found, use the sign up option")
        elif validate == 'invalid_password':
            return render_template('sign_in.html', error="Incorrect password")
        else:
            session['e_mail'] = e_mail
            stored_url = session.pop('store', None)
            if stored_url:
                #render_template('', userS=userS[0])
                return redirect(stored_url)
            else:
                return redirect(url_for('kasu.main'))

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
        check = db.verify_mail(e_mail)
        if check == 'found':
            return render_template('sign_up.html', error="e_mail already registered, please use sign_in option")
        else:
            db.new_user(reg)
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
                userid = db.get_active_userID(email)
                userS = db.get_active_user(session['e_mail'])
                retriveProducts = db.cartProductIDs(userid[0])
            if len(cart) == 0 and len(retriveProducts) == 0:
                return render_template('shoping_cart.html', count=0)
            else:
                cart_list = retriveProducts
                increase = len(retriveProducts)
                if len(cart) > 0:
                    for pid in cart:
                        increase += 1
                        catid = db.get_catID(pid['pid'])
                        qty = pid['qty']
                        db.addToCart(pid['pid'], catid[0], userid[0], qty)
                    newlist = db.cartProductIDs(userid[0])
                    for content in newlist:
                        gotten = db.view_product(content[0])
                        lis.append([gotten, content[1]])
                else:
                    for content in cart_list:
                        gotten = db.view_product(content[0])
                        lis.append([gotten, content[1]])                    
                     
            return render_template('shoping_cart.html', lis=lis, count=increase, userS=userS[0])
        return cart_get()
        
    elif request.method == 'POST':
        pid = request.form.get('productid')
        qty = request.form.get('quantity')
        
        cartSelect = {'pid':pid, 'qty':qty}

        cart.append(cartSelect)
        session['cart'] = cart
        return 'Successful'
    
@start.route('/kasuwa/cart/order', methods=['POST', 'GET'])
@login_required
def order():
    """Order your items from cart only when you are signed in"""
    userProducts = []
    quantity = []
    returnList = []
    if request.method == 'POST':
        items = request.form.get('order')
        items = items.split(',')
        qtyty = request.form.get('qtity')
        payValue = request.form.get('payOrder')
        for x in qtyty:
            try:
                quantity.append(int(x))
            except Exception:
                pass
        for z in items:
            try:
                getid = (int(z))
                pd = db.view_product(getid)
                userProducts.append(pd)
            except Exception:
                pass
        for cnt in range(len(quantity)):
            new = [quantity[cnt], userProducts[cnt]]
            returnList.append(new)
               
        return render_template('order.html', myOrders=returnList, amount=payValue)
    elif request.method == 'GET':
        print(userProducts)
        return render_template('order.html', myOrders=userProducts)

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
        renderCart = db.view_product(productID)
        return render_template('product.html', productInView=renderCart, time=time)

@start.route('/kasuwa/cart/delete', methods=['GET', 'POST'])
def delete():
    """Delete item from cart"""
    if request.method == 'GET':
        return None
    elif request.method == 'POST':
        productid = request.form.get('delid')
        db.delCartItem(productid)
    return 'Success'

def pwdUrl(url):
    """store present user URL"""
    session['store'] = url
