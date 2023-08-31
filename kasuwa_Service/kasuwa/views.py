from flask import Blueprint, render_template

views = Blueprint('Views', __name__)

@views.route('/home')
def home():
    return render_template("index.html")