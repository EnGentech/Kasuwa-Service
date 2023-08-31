from models.category import Category
from models.cart import Cart
from models.comment import Comment
from models.product import Product
from models.rating import Rating
from models.transaction import Transaction
from models.user import User
from run_main import session


class Db_Management:
    """Define all funtions regarding database management"""
    classes = {
        'Category': Category,
        'Cart': Cart,
        'Comment': Comment,
        'Product': Product,
        'Rating': Rating,
        'Transaction': Transaction,
        'User': User
    }

    def __init__(self) -> None:
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
