from flask import Blueprint

views = Blueprint('Views', __name__)

@views.route('/')
def home():
    return ("<h1>Test<h1>")