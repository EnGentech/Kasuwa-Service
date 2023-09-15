# from flask import Blueprint, jsonify
# from .models import Product
# from .Base_connect import session

# js_app = Blueprint('js_app', __name__)

# @js_app.route('/api/product/<int:product_id>')

# def add_to_cart(product_id):
#     product = session.query(Product).filter_by(id=product_id).first()
#     print('Here')
#     print(product)
#     if product:
#         product_data = product.to_dict()
#         return jsonify(product_data)
#     else:
#         return({'error': 'product not found'}), 404