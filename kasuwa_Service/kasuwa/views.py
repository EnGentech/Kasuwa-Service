from flask import Blueprint, render_template
from flask_login import login_required
from .models import Category, Product
from .Base_connect import session

views = Blueprint('Views', __name__)

@views.route('/')
def Landing_page():
    return render_template("landing.html")

@views.route('/home')
def index():
    categories = session.query(Category).all()
    products = session.query(Product).all()
    # product = session.query(Product).filter_by(id=product.id)
    for prod in products:
        print(prod.name)
    return render_template('index.html', categories=categories, products=products)
    


@views.route('/category/<category_name>')
def category(category_name):
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        products = session.query(Product).filter_by(category_id=category.id).all()
        if products:
            return render_template(f'{category_name}.html', products=products, category=category) 
        return render_template('cat.html', category=category)
    else:
        # Handle the case when the category does not exist
        return "Category not found", 404
    

@views.route('/shopping_cart/')
@login_required
def shopping_cart():
    product = session.query(Product).first()
    return render_template('shopping_cart.html', product=product)

@views.route('/product/<int:product_id>')
def product_details(product_id):
    product = session.query(Product).filter_by(id=product_id).first()
    return render_template('product_details.html', product=product)
