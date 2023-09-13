# from .models import Base, User, Comment, Product, Transaction, Category, Cart, Rating, Billing_address, Order
# from .Base_connect import session
# from datetime import datetime

# # Create instances of your classes
# def add_user(username, fullname, email, password, address, phone, gender):
#     user = User(
#         username=username, 
#         fullname=fullname, 
#         email=email,
#         password=password,
#         address=address,
#         phone=phone,
#         gender=gender, 
#         birthDate = datetime.strptime('2000-01-01', '%Y-%m-%d').date()
#         )
#     session.add(user)
#     session.commit

# category = Category(
#     category='Electronics'
#     )
# session.add(category)
# session.commit

# product = Product(
#     name='Laptop', 
#     type='Electronics', 
#     description='A powerful laptop', 
#     stock=10, 
#     price=1000, 
#     category=category,
#     user=user,
#     image_source="Imagelab"
# )
# comment = Comment(
#     comment='This is a comment',
#     user=user,
#     product=product,
#     category=category
# )
# transaction = Transaction(
#     quantity=2, 
#     approval_status='Approved', 
#     user=user,
#     category=category
#     )
# cart = Cart(
#     quantity=3, 
#     user=user, 
#     category=category
# )
# rating = Rating(
#     value=4, 
#     user=user, 
#     category=category,
#     product=product
# )
# billing_address = Billing_address(
#     user=user, 
#     bill_address='123 Main St'
# )
# order = Order(
#     name='Order 1', 
#     user=user, 
#     product=product,
#     transaction=transaction, 
#     category=category
# )

# # Populate the association table
# product.transaction.append(transaction)
# product.cart.append(cart)
# # Commit the changes to the session
# session.commit()



# # Add instances to the session
# session.add(user)
# session.add(comment)
# session.add(category)
# session.add(product)
# session.add(transaction)
# session.add(cart)
# session.add(rating)
# session.add(billing_address)
# session.add(order)

# # Commit the session to persist the data
# session.commit()

# # Close the session
# session.close()