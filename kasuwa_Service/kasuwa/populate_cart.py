# from datetime import datetime
# from models import User, Cart, Category
# from sqlalchemy.orm import Session
# from Base_connect import engine
# from Base_connect import session

# user1 = session.query(User).filter(User.id==1).first()
# print (user1)
# user2 = session.query(User).filter(User.id==2).first()
# print (user2)
# product = session.query(Product).filter(Product.id == 1).first()

# category = session.query(Category).filter(Category.id == 1).first()

# if user1:
#     cart = Cart(user=user1, quantity=2)
#     session.add(cart)
#     session.commit()

# category = Category(category='Sample Category')
# username = "john_doe"
# user = session.query(User).filter_by(username=username).first()
# cart = Cart(user=user, category=category, quantity=1)

# session.add(cart)
# session.commit()
# session.close()