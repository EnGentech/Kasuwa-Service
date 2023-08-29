from base import Base, BaseModel, engine, Session
from billing_address import BillingAddress
from cart import Cart
from category import Category
from cartItems import CartItems
from comments import Comments
from ordered_items import OrderItem
from order import Order
from user import User
from product import Product
from transaction import Transaction
from rating import Rating


Base.metadata.create_all(engine)

session = Session()

# adding users
user1 = User(username="barth10", fullname="barth bassey", email="bb@gmail.com")
user2 = User(username="barth12", fullname="good bas", email="ba@gmail.com")

# adding category
electronic = Category(title="Electronic")
gadget = Category(title="gadget")
fashion = Category(title="fashion")


#adding products
women_jean = Product(
    product_name ="women jeans", 
    description = "blue strong jeans",
    specification = "blue strong jeans",
    stock = 89,
    price = 6000,
    image_url = "https://www.image.com",
    categories = fashion

)
men_jean = Product(
    product_name ="women jeans", 
    description = "blue strong jeans",
    specification = "blue strong jeans",
    stock = 89,
    price = 6000,
    image_url = "https://www.image.com",
    categories = fashion
)
television = Product(
    product_name ="lg television", 
    description = "flat curve screen tv a product of lg",
    specification = "51inch size tv",
    stock = 100,
    price = 50000,
    image_url = "https://www.image.com",
    categories = electronic
)

five_star = Rating(
    rating = 4.5,
    product = television,
    user = user1
)

four_star = Rating(
    rating = 4.0,
    product = men_jean,
    user = user2
)

three_star = Rating(
    rating = 3.5,
    product = men_jean,
    user = user1

)
address1_user1 = BillingAddress(
    phoneNumber = '0813356754',
    billing_address = 'plot 24 , kuje street',
    user = user1
)

address1_user2 = BillingAddress(
    phoneNumber = '08133533333',
    billing_address = 'plot 27 , mataima street',
    user = user2
)

address2_user1 = BillingAddress(
    phoneNumber = '08133566666',
    billing_address = 'plot 24 , Ecwa street',
    user = user1
)
items1 = CartItems(
    quantity = 10,
    # cart = cart_user1,
    product = men_jean

)
items2 = CartItems(
    quantity = 1,
    # cart = cart_user1,
    product = television

)
items3 = CartItems(
    quantity = 2,
    # cart = cart_user2,
    product = television

)
cart_user1 = Cart(
    user = user1,
    items = items1

)

cart_user2 = Cart(
    user = user2,
    items = items1

)
cart_user3 = Cart(
    user = user2,
    items = items3

)

# comment_user1 = Comments(
#     message = "Bad product",
#     user = user1,
#     products = men_jean
# )

# comment_user2 = Comments(
#     message = "Good product",
#     user = user2,
#     products = men_jean
# )

# comment_user3 = Comments(
#     message = "Bad product",
#     user = user1,
#     products = television
# )
order_items1 = OrderItem(
    quantity = 2,
    Price_per_item = 3,
    product = men_jean,
    user = user1
)

order_items2 = OrderItem(
    quantity = 2,
    Price_per_item = 3,
    product = television,
    user = user1
)

order_items3 = OrderItem(
    quantity = 2,
    Price_per_item = 3,
    product = television,
    user = user2
)

order1 = Order(
    user = user1,
    shipping_address = address1_user1,
    order_item = order_items1
)
order2 = Order(
    user = user2,
    shipping_address = address1_user2,
    order_item = order_items2
)

order3 = Order(
    user = user1,
    shipping_address = address2_user1,
    order_item = order_items3
)

# transaction1 = Transaction(
#     payment_method='Card',
#     transaction_status = 'Approved',
#     total_amount = 10000.78,
#     user = user1,
#     order = order1
# )
# transaction2 = Transaction(
#     payment_method='Card',
#     transaction_status = 'Approved',
#     total_amount = 80000.78,
#     user = user2,
#     order = order2
# )
#
#persist data
session.add(user1)
session.add(user1)

session.add(electronic)
session.add(gadget)
session.add(fashion)

session.add(women_jean)
session.add(men_jean)
session.add(television)

session.add(four_star)
session.add(five_star)
session.add(three_star)

session.add(address1_user1)
session.add(address1_user1)
session.add(address2_user1)

session.add(items1)
session.add(items2)
session.add(items3)

session.add(cart_user1)
session.add(cart_user2)
session.add(cart_user3)

# session.add(comment_user1)
# session.add(comment_user2)
# session.add(comment_user3)

session.add(order_items1)
session.add(order_items2)
session.add(order_items3)

session.add(order1)
session.add(order2)
session.add(order3)

# session.add(transaction1)
# session.add(transaction2)


session.commit()
session.close()