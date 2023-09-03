from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
views = Blueprint('Views', __name__)

@views.route('/home')
@login_required
def index():
    
    categories = [
        {"name": "Women's Fashion", "icon": "fa-brands fa-gitlab", "color": "#96999c"},
        {"name": "Men's Fashion", "icon": "fa-solid fa-shirt", "color": "#96999c"},
        {"name": "Phone's & Telecommunications", "icon": "fa-solid fa-mobile-screen-button", "color": "#96999c"},
        {"name": "Computer, Ofice & Security", "icon": "fa-solid fa-desktop", "color": "#96999c"},
        {"name": "Cunsumer Electronics", "icon": "fa-solid fa-radio", "color": "#96999c"},
        {"name": "Jewelry & Watches", "icon": "fa-solid fa-ring", "color": "#96999c"},
        {"name": "Home, pet & Appliances", "icon": "fa-solid fa-house-chimney", "color": "#96999c"},
        {"name": "Bags & Shoes", "icon": "fa-solid fa-bag-shopping", "color": "#96999c"},
        {"name": "Toys, Kids & Babies", "icon": "fa-solid fa-gamepad", "color": "#96999c"},
        {"name": "Outdoor Fun & Sports", "icon": "fa-solid fa-football", "color": "#96999c"},
        {"name": "Beauty, Health & Hair", "icon": "fa-solid fa-vest", "color": "#96999c"},
        {"name": "Automobiles & Motorcycles", "icon": "fa-solid fa-bycycle", "color": "#96999c"},
        {"name": "Tools & Home Improvement", "icon": "fa-solid fa-screwdriver-wrench", "color": "#96999c"}
    ]

    clicked_category = request.args.get('category')
    if clicked_category == categories[0]['name']:
        return render_template('product.html')
    if clicked_category == categories[1]['name']:
        return render_template('product.html')
    if clicked_category == categories[2]['name']:
        return render_template('product.html')
    if clicked_category == categories[3]['name']:
        return render_template('product.html')
    if clicked_category == categories[4]['name']:
        return render_template('product.html')
    if clicked_category == categories[5]['name']:
        return render_template('product.html')
    if clicked_category == categories[6]['name']:
        return render_template('product.html')


    return render_template("index.html", categories=categories, user=current_user)
