# from models import User, Product, Transaction, Category
# from Base_connect import session


# user = session.query(User).filter_by(username='john_doe').first()
# product = session.query(Product).filter_by(name='Sample Product').first()
# category = session.query(Category).filter_by(category='Sample Category').first()

# new_transaction = Transaction(
#     user=user,
#     product=[product], 
#     category_id=category.id,         
#     quantity=2,
#     approval_status='approved'
# )

# session.add(new_transaction)
# session.commit()

