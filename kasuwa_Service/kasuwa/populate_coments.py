# from models import User, Comment, Product, Category
# from Base_connect import session

# user = session.query(User).filter_by(username='john_doe').first()
# product = session.query(Product).filter_by(name='Sample Product').first()
# category = session.query(Category).filter_by(category='Sample Category').first()


# new_comment = Comment(comment='New sample comment', user=product.user)

# product.comments.append(new_comment)
# category.comments.append(new_comment)

# session.add(new_comment)
# session.commit()
