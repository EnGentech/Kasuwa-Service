# from models import User, Product, Category
# from Base_connect import session


# username = "john_doe"
# user = session.query(User).filter_by(username=username).first()


# category = Category(category='Sample Category')
# new_product = Product(
#     name='Sample Product',
#     type='Type',
#     description='Sample description',
#     stock=10,
#     price=100,
#     user=user, 
#     category=category, 
#     image_source='favourlab'
# )

# session.add(Product)
# session.commit()
# session.close()