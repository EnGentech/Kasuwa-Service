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
from flask import g

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
        self.__session.flush()
        self.save()

    def new_billingAddress(self, getid, data):
        """This method create new billing address for a user in session"""
        new_address = BillingAddress(
            nationality=data['nation'],
            contact_name=data['contactName'],
            mobile_number=data['mobile'],
            address=data['address'],
            state=data['state'],
            lga=data['lga'],
            zip_code=data['zip'],
            user_id=getid
            )
        try:
            self.__session.add(new_address)
            self.__session.flush()
        except Exception as e:
            self.__session.rollback()
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
        
    def get_active_user(self, email):
        """this function will active user"""
        user = self.__session.query(User.username).filter_by(email=email).first()
        return user
    
    def category(self):
        """get all data from catetory and store to a dictionary"""
        cat_items = {}
        cats = self.__session.query(Category).all()
        if cats:
            for cat in cats:
                cat_items[cat.category] = [cat.icon, cat.id, cat.category]
            return cat_items
        
    def product_category(self, cat_id):
        """return the entire product for a category"""
        prod_cart_items = {}
        prod = self.__session.query(Product).filter_by(category_id=cat_id).all()
        if prod:
            for prods in prod:
                value = prods.price
                new_value = str(value).split('.')
                mydict = {
                    'prodID': prods.id,
                    'cartID': prods.category_id,
                    'name': prods.product_name,
                    'type': prods.product_type,
                    'description': prods.description,
                    'naira': '{:,}'.format(int(new_value[0])),
                    'kobo': '{:02}'.format(int(new_value[1])),
                    'image': prods.image_source,
                    'stock': prods.stock
                }
                prod_cart_items[prods.id] = mydict
            return prod_cart_items
        
    def view_product(self, prodid):
        """View user selected product in details"""
        choice = self.__session.query(Product).filter_by(id=prodid).first()
        if choice:
            value = choice.price
            new_value = str(value).split('.')
            productInfo = {
                "id": choice.id,
                "name": choice.product_name,
                'description': choice.description,
                'naira': '{:,}'.format(int(new_value[0])),
                'kobo': '{:02}'.format(int(new_value[1])),
                'image': choice.image_source,
                'stock': choice.stock,
                'type': choice.product_type
            }
            return productInfo
        else:
            print("nothing selected")

    def get_active_userID(self, email):
        """this function will active user"""
        userID = self.__session.query(User.id).filter_by(email=email).first()
        return userID
    
    def get_catID(self, productID):
        """this function will active user"""
        catID = self.__session.query(Product.category_id).filter_by(id=productID).first()
        return catID
            
    def addToCart(self, productids, categoryids, userids, qty):
        """Get product ids and populate database"""
        addtoDB = Cart(product_id=productids, category_id=categoryids, user_id=userids, quantity=qty)
        self.__session.add(addtoDB)
        self.save()
        self.__session.close()

    def cartProductIDs(self, userID):
        """Retrieve all products Id for listing cart"""
        allPD = self.__session.query(Cart.product_id, Cart.quantity).filter_by(user_id=userID).all()
        return allPD
    
    def delCartItem(self, productid):
        """Delete data product from cart"""
        delItem = self.__session.query(Cart).filter_by(product_id=productid).first()
        self.__session.delete(delItem)
        self.__session.commit()
        self.save()
    
    def getBillingAddresses(self, userID):
        """retrive all addresses of a user in session"""
        addressList = self.__session.query(BillingAddress).filter_by(user_id=userID).all()
        return addressList