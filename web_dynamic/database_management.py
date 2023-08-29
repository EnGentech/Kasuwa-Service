from models.category import Category
from models.cart import Cart
from models.comment import Comment
from models.product import Product
from models.rating import Rating
from models.transaction import Transaction
from models.user import User
from models.orders import OrderItems
from models.billing_address import BillingAddress
from createModels import session
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class Db_Management:
    """Define all funtions regarding database management"""
    classes = {
        'Category': Category,
        'Cart': Cart,
        'Comment': Comment,
        'Product': Product,
        'Rating': Rating,
        'Transaction': Transaction,
        'User': User,
        'OrderItems': OrderItems,
        'BillingAddress': BillingAddress
    }

    def __init__(self):
        """creating initialize variables"""
        self.__session = session

    def delete(self, clas, id):
        """delete category with products associated through its id""" 
        if clas in self.classes:
            try:
                clas_instance = self.__session.query(self.classes[clas]).get(id)
                self.__session.delete(clas_instance)
                self.save()
            except Exception:
                return "No instance of Id found"
        else:
            return "Not a valid class"
    
    def save(self):
        """a function defined to commit to the database"""
        self.__session.commit()

    def new_user(self, new):
        """create new user into database"""
        new_user = User(username=new[0], email=new[1], password=new[2], phone_number=new[3])
        self.__session.add(new_user)
        self.save()

    def verify_mail(self, mail):
        """check is email exist in database"""
        found = self.__session.query(User).filter_by(email=mail).first()
        if found:
            return 'found'
        
    def authenticate(self, email, passcode):
        """Authenticate user sign_in credentials"""
        e_mail = self.__session.query(User).filter_by(email=email).first()
        if e_mail == False and bcrypt.check_password_hash(e_mail.password, passcode) == False:
            return 'invalid_credentials'
        elif e_mail:
            if bcrypt.check_password_hash(e_mail.password, passcode):
                return 'allow_access'
            else:
                return "invalid_password"
        else:
            return "invalid_email"