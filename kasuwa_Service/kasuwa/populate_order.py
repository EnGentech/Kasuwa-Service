# from datetime import datetime
# from models import User, Product, Transaction, Category, Order
# from sqlalchemy.orm import Session
# from Base_connect import engine
# from Base_connect import session

# user = session.query(User).filter_by(username='john_doe').first()
# transaction = session.query(Transaction).filter_by(user=user).first()
# product = session.query(Product).filter_by(name='Sample Product').first()
# category = session.query(Category).filter_by(category='Sample Category').first()

# # Create a new order and populate the fields
# new_order = Order(
#     name='Sample Order',
#     transaction_id=transaction.id,
#     user=user,
#     product_id=product.id,
#     category_id=category.id
# )

# session.add(new_order)
# session.commit()