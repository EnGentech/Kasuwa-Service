from sqlalchemy import Table, Column, String, Integer, Date, Float, LargeBinary
from .Base_connect import Base, session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin

class User(Base, UserMixin):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(length=50), nullable=False)
    fullname = Column(String(length=50), nullable=False)
    email = Column(String(length=50), unique=True, nullable=False)
    password = Column(String(length=150))
    address = Column(String(length=200))
    phone = Column(String(length=20))
    image_source = Column(LargeBinary)  # Added image_source field for the user
    comments = relationship("Comment", back_populates="user")
    ratings = relationship("Rating")
    billing_address = relationship("Billing_address", back_populates="user")
    carts = relationship("Cart", back_populates="user")
    products = relationship("Product", back_populates="user", primaryjoin="User.id == Product.user_id")
    transactions = relationship("Transaction")
    orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"<User {self.fullname}>"

class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True)
    comment = Column(String(length=200))
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    user = relationship("User", back_populates="comments")
    category = relationship("Category", back_populates="comments")
    product = relationship("Product", back_populates="comments")

    def __repr__(self):
        return f"<C {self.comment}>"

products_Transactions = Table('product_trans', 
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('transaction_id', Integer, ForeignKey('transactions.id'))
)

cart_prod = Table('cart_product', 
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('cart_id', Integer, ForeignKey('carts.id'))
)

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    type = Column(String(20), nullable=False)
    description = Column(String(200), nullable=False)
    stock = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)  # Changed to Float data type
    transaction = relationship("Transaction", secondary=products_Transactions, overlaps="transaction")
    cart = relationship("Cart", secondary=cart_prod, overlaps="cart")
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="products")
    comments = relationship("Comment", back_populates="product")
    image_source = Column(LargeBinary)  # Changed to LargeBinary data type
    date = Column(Date)  # Added a date field
    order = relationship("Order", back_populates="product")

    def __repr__(self):
        return f"<Productname {self.name}>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'description': self.description,
            'stock': self.stock,
            'price': self.price,
            'category_id': self.category_id,
            'date':self.date,
            'image': self.image_source
        }



class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="transactions")
    product = relationship("Product", secondary=products_Transactions, overlaps="transaction")
    category = relationship("Category")
    category_id = Column(Integer, ForeignKey('categories.id'))
    quantity = Column(Integer)
    approval_status = Column(String(10), nullable=False)
    orders = relationship("Order", back_populates="transaction")

    def __repr__(self):
        return f"<User {self.__name__}>"

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    icon = Column(String(100))
    colour = Column(String(100))

    ratings = relationship("Rating", back_populates="category")
    cart = relationship("Cart", back_populates="category")
    comments = relationship("Comment", back_populates="category")
    orders = relationship("Order", back_populates="category")

    def __repr__(self):
        return f"<User {self.name}>"

class Cart(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="carts")
    product = relationship("Product", secondary=cart_prod, overlaps="cart")
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="cart")
    cart = relationship("Product", secondary=cart_prod, overlaps="product")
    quantity = Column(Integer)

    def __repr__(self):
        return f"<User {self.quantity}>"
class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="ratings")
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product")
    user = relationship("User", back_populates="ratings")
    value = Column(Integer)

    def __repr__(self):
        return f"<User {self.value}>"
    
class Billing_address(Base):
    __tablename__ = "billing_address"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")
    bill_address = Column(String(45), nullable=False)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    transaction_id = Column(Integer, ForeignKey('transactions.id'))
    category_id = Column(Integer, ForeignKey("categories.id"))
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    date = Column(Date)
    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="order")
    category = relationship("Category", back_populates="orders")
    transaction = relationship("Transaction", back_populates="orders")


from .Base_connect import session
# categories = session.query(Category).all()

# categories = [
#     Category(name = 'Women\'s Fashion', icon = 'fa-brands fa-gitlab', colour = '#96999c'),
#     Category(name = 'Men\'s Fashion', icon = 'fa-solid fa-shirt', colour = '#96999c'),
#     Category(name = 'Phone\'s & Telecommunications', icon = 'fa-solid fa-mobile-screen-button', colour = '#96999c'),
#     Category(name = 'Computer, Ofice & Security', icon = 'fa-solid fa-desktop', colour = '#96999c'),
#     Category(name = 'Cunsumer Electronics', icon = 'fa-solid fa-radio', colour = '#96999c'),
#     Category(name = 'Jewelry & Watches', icon = 'fa-solid fa-ring', colour = '#96999c'),
#     Category(name = 'Home, pet & Appliances', icon = 'fa-solid fa-house-chimney', colour = '#96999c'),
#     Category(name = 'Bags & Shoes', icon = 'fa-solid fa-bag-shopping', colour = '#96999c'),
#     Category(name = 'Toys, Kids & Babie', icon = 'fa-solid fa-gamepad', colour = '#96999c'),
#     Category(name = 'Outdoor Fun & Sports', icon = 'fa-solid fa-football', colour = '#96999c'),
#     Category(name = 'Beauty, Health & Hair', icon = 'fa-solid fa-vest', colour = '#96999c'),
#     Category(name = 'Automobiles & Motorcycles', icon = 'fa-solid fa-bicycle', colour = '#96999c'),
#     Category(name = 'Tools & Home Improvement', icon = 'fa-solid fa-screwdriver-wrench', colour = '#96999c'),
#     ]

# for category_instance in categories:
#     session.add(category_instance)
# session.commit()
# session.close()
# print('Categories populated successfully!')
# import os
from datetime import datetime
# data = [
#     (1, "Floral Maxi Dress", "dress", "Elegant floral maxi dress for women. Perfect for weddings, parties, or a night out. Made with high-quality materials for comfort and style.", 150, 8200.00, "floral_maxi_dress.jpg", "2023-09-12"),
#     (1, "High-Waisted Skinny Jeans", "jeans", "Stylish high-waisted skinny jeans for a flattering fit. Versatile and comfortable, suitable for both casual and formal occasions.", 200, 6400.00, "high_waisted_jeans.jpg", "2023-09-12"),
#  
# data = [
#     (2, 'Body_fitted polo', 'polo', 'let the world feel your masculinity by using this attractive awesome nice sexy sweet polo', 7223, 7202.55, "2023-09-12"),
#     (2, 'Italian shirts', 'shirt', 'Dress like a smart niggi, get the best quality product here', 50400, 52034.45, "2023-09-12"),
#     (2, 'Italian shoes', 'shoe', 'Your shoes speaks more of your dressing, Dress like a smart niggi, get the best quality product here', 5400, 3400.45, "2023-09-12"),
#     (2, 'Italian shirts', 'shirt', 'Dress like a smart niggi, get the best quality product here', 50400, 52034.45, "2023-09-12"),
#     (2, 'Quality wrist watch', 'watch', 'You cant be complete without a perfect wrist watch, get one today', 50400, 2480.45, "2023-09-12"),
#     (2, 'rocket boxers', 'boxer', 'cover your odogu while getting a bit of attraction, only if you a man i mean a man', 55400, 7500.55, "2023-09-12"),
#     (2, 'Channels quality bag', 'bag', 'Dont use urgly bags, you will not make heaven, get a good one today', 25899, 2500.00, "2023-09-12"),
#     (2, 'UI/UX shoes', 'shoeUI', 'Do you think italian is the best shoe?, then you are yet to try UI/UX, your number one in quality', 50400, 3500.25, "2023-09-12"),
#     (2, 'London Polo', 'polo_london', 'You dont need to go to US before getting quality designers, kasuwa service, your priority', 50400, 5300.45, "2023-09-12"),
#     (2, 'Peace Underwear', 'underwear', 'when we call it white then its white, we talk less and give quality', 23522, 4800.95, "2023-09-12"),
#     (2, 'sporty face-cap', 'faceCap', 'Get fitted with sport, all work with no play, my brother you are doll', 259000, 3500.55, "2023-09-12"),
#     (2, 'Peacat Sucks', 'sucks', 'Dress like a smart niggi, get the best quality product here', 50400, 325.45, "2023-09-12"),
#     (2, 'Designers boxers', 'boxer_design', 'cover your odogu while getting a bit of attraction, only if you a man i mean a man. With our product, the fear of disgrace when you see good looks is covered', 55400, 2750.55, "2023-09-12")
# ]

# data = [
#     (3, "iPhone 13 Pro", "smartphone1", "The latest iPhone with advanced camera and performance. Experience the power of A15 Bionic chip and ProRAW photography.", 300, 9929.10, "2023-09-12"),
#     (3, "Samsung Galaxy S21", "smartphone2", "A flagship Android smartphone with stunning display and 5G capabilities. Capture the future with Samsung Galaxy S21.", 400, 7929.10, "2023-09-12"),
#     (3, "Google Pixel 7", "smartphone3", "Capture incredible photos with the Google Pixel 7's advanced camera system. A smartphone designed for photography enthusiasts.", 200, 7199.10, "2023-09-12"),
#     (3, "OnePlus 9 Pro", "smartphone4", "Experience lightning-fast performance with the OnePlus 9 Pro powered by Snapdragon 888. Seamless multitasking at your fingertips.", 250, 2499.10, "2023-09-12"),
#     (3, "Motorola Edge", "smartphone5", "A feature-packed smartphone at an affordable price. Enjoy a large display, long-lasting battery, and versatile camera.", 500, 4939.10, "2023-09-12"),
#     (3, "Sony Xperia 1 III", "smartphone5", "Sony's flagship phone with 4K display and pro camera features. Elevate your mobile entertainment and photography game.", 150, 1099.10, "2023-09-12"),
#     (3, "Apple Watch Series 7", "smart_watch", "Stay connected and track your health with the Apple Watch Series 7. It's more than a watch; it's a lifestyle companion.", 350, 2099.10, "2023-09-12"),
#     (3, "Samsung Galaxy Watch 4", "smart_watch", "A versatile smartwatch with fitness tracking, AMOLED display, and long battery life. Your perfect companion for an active life.", 400, 2149.09, "2023-09-12"),
#     (3, "Fitbit Versa 3", "smart_watch", "Monitor your fitness goals with the Fitbit Versa 3. Stylish, comfortable, and packed with health features for an active lifestyle.", 300, 1990.49, "2023-09-12"),
#     (3, "Bose Noise-Cancelling Headphones", "headphones", "Enjoy immersive sound with noise-cancelling technology. Escape into your world of music with premium Bose headphones.", 700, 3149.29, "2023-09-12"),
#     (3, "Sony WH-1000XM4 Headphones", "headphones", "Experience premium audio quality with Sony headphones. Noise cancellation, comfort, and style in one package.", 500, 2929.23, "2023-09-12"),
#     (3, "JBL Bluetooth Speaker", "speaker", "Take your music anywhere with a portable JBL speaker. High-quality sound and durability for your on-the-go lifestyle.", 800, 719.91, "2023-09-12"),
#     (3, "Logitech Webcam", "webcam", "Upgrade your video calls with a high-quality Logitech webcam. Crystal-clear video and audio for professional communication.", 400, 809.69, "2023-09-12"),
# ]
# data = [
#     (4, 'Dell XPS 13 Laptop', 'laptop', 'Experience powerful performance with the Dell XPS 13 laptop', 300, 1199.36,"2023-09-12"),
#     (4, 'HP EliteBook 840 G7', 'laptop', 'A reliable and secure business laptop for professionals', 200, 9990.21, "2023-09-12"),
#     (4, 'Microsoft Surface Pro 7', 'tablet', 'Versatile 2-in-1 tablet for work and entertainment', 400, 7929.12,"2023-09-12"),
#     (4, 'Epson EcoTank ET-4770', 'printer', 'High-capacity ink tank printer for cost-effective printing', 150, 3909.30,  "2023-09-12"),
#     (4, 'Logitech Wireless Keyboard', 'keyboard', 'Comfortable and reliable wireless keyboard for productivity', 500, 419.30, "2023-09-12"),
#     (4, 'Steelcase Gesture Chair', 'office_chair', 'Ergonomic office chair for maximum comfort during work', 100, 4990.25,"2023-09-12"),
#     (4, 'Lenovo ThinkCentre Desktop', 'desktop', 'Powerful desktop computer for office tasks and more', 200, 7929.20, "2023-09-12"),
#     (4, 'Netgear Nighthawk Router', 'router', 'Fast and reliable router for home and small office use', 300, 1049.00, "2023-09-12"),
#     (4, 'Canon EOS 5D Mark IV', 'camera', 'Professional DSLR camera for high-quality photography', 100, 2499.00,"2023-09-12"),
#     (4, 'Samsung 27-Inch Monitor', 'monitor', 'Crisp and vibrant display for improved productivity', 250, 1099.21, "2023-09-12"),
#     (4, 'Fireproof Document Safe', 'safe', 'Protect your important documents with a fireproof safe', 150, 1449.20,"2023-09-12"),
#     (4, 'Norton 370 Antivirus', 'antivirus', 'Comprehensive antivirus software for security', 500, 509.25,"2023-09-12"),
#     (4, 'Canon PIXMA All-in-One Printer', 'printer', 'Affordable all-in-one printer for home and office use', 300, 8190.45, "2023-09-12"),
#     (4, 'Wireless IP Security Camera', 'security_camera', 'Keep an eye on your property with a wireless security camera', 400, 791.25, "2023-09-12"),
#     (4, 'Dell UltraSharp 4K Monitor', 'monitor', 'High-resolution 4K monitor for professional graphics work', 200, 799.12, "2023-09-12"),
#     (4, 'HP LaserJet Pro Printer', 'printer', 'Fast and efficient laser printer for office documents', 300, 1099.24, "2023-09-12"),
# ]
# data = [
#     (5, 'Smartphone X', 'smartphone', 'The latest flagship smartphone with cutting-edge features', 500, 7919.10, '2023-09-12'),
#     (5, 'Tablet Pro', 'tablet', 'A high-performance tablet for work and entertainment', 300, 4990.10, '2023-09-12'),
#     (5, 'Ultra HD TV', 'television', 'Experience stunning visuals with our Ultra HD television', 500, 5499.10, '2023-09-12'),
#     (5, 'Gaming Console', 'gaming_console', 'Take your gaming experience to the next level with our console', 200, 3099.10, '2023-09-12'),
#     (5, 'Laptop Pro', 'laptop', 'Powerful laptop for work and gaming on the go', 400, 5099.10, '2023-09-12'),
#     (5, 'Wireless Earbuds', 'earbuds', 'Enjoy music without the hassle of wires with our wireless earbuds', 800, 999.10, '2023-09-12'),
#     (5, 'Smart Watch', 'smart_watch', 'Stay connected and track your fitness with our smartwatch', 300, 5991.10, '2023-09-12'),
#     (5, 'Digital Camera', 'camera', 'Capture stunning moments with our high-resolution digital camera', 550, 5926.10, '2023-09-12'),
#     (5, 'Bluetooth Speaker', 'speaker', 'Enhance your audio experience with our portable Bluetooth speaker', 500, 490.10, '2023-09-12'),
#     (5, 'Wireless Router', 'router', 'Experience blazing-fast internet speeds with our wireless router', 200, 7109.10, '2023-09-12'),
#     (5, 'Smart Home Hub', 'smart_home', 'Control your smart home devices with ease using our hub', 500, 5419.10, '2023-09-12'),
#     (5, 'VR Headset', 'vr_headset', 'Immerse yourself in virtual reality with our VR headset', 550, 2919.10, '2023-09-12'),
#     (5, 'Portable Power Bank', 'power_bank', 'Never run out of battery with our portable power bank', 5000, 292.10, '2023-09-12'),
#     (5, 'External Hard Drive', 'hard_drive', 'Expand your storage capacity with our reliable external hard drive', 300, 790.10, '2023-09-12'),
#     (5, 'Wireless devices', 'keyboard_mouse', 'Stay productive with our wireless keyboard and mouse combo', 500, 8500.10, '2023-09-12'),
#     (5, 'Smart Thermostat', 'thermostat', 'Efficiently control your home\'s temperature with our smart thermostat', 200, 529.10, '2023-09-12'),
#     (5, 'Drone Pro', 'drone', 'Capture breathtaking aerial footage with our professional drone', 500, 799.10, '2023-09-12'),
#     (5, 'Fitness Tracker', 'fitness_tracker', 'Track your fitness goals and stay active with our fitness tracker', 400, 59.10, '2023-09-12'),
#     (5, 'Electric Scooter', 'scooter', 'Effortlessly commute with our electric scooter', 200, 299.10, '2023-09-12'),
#     (5, 'Smart Home Camera', 'home_camera', 'Keep an eye on your home with our smart home camera', 300, 529.10, '2023-09-12')
# ]

# data = [
#     (6, "Diamond Solitaire Necklace", "necklace", "Elegant diamond solitaire necklace for special occasions", 100, 1999.10, "2023-09-12"),
#     (6, "Men's Stainless Steel Watch", "watch", "Stylish stainless steel watch with a timeless design", 200, 499.10, "2023-09-12"),
#     (6, "Sapphire and Diamond Earrings", "earrings", "Beautiful sapphire and diamond earrings for a touch of luxury", 150, 1499.10, "2023-09-12"),
#     (6, "Gold Engagement Ring", "ring", "Exquisite gold engagement ring with a sparkling diamond", 50, 2999.10, "2023-09-12"),
#     (6, "Pearl Strand Bracelet", "bracelet", "Classic pearl strand bracelet for a timeless look", 100, 599.10, "2023-09-12"),
#     (6, "Automatic Skeleton Watch", "watch", "A unique automatic skeleton watch with a see-through design", 100, 799.10, "2023-09-12"),
#     (6, "Emerald and Diamond Ring", "ring", "Dazzling emerald and diamond ring for special occasions", 75, 2499.10, "2023-09-12"),
#     (6, "Rose Gold Bangle", "bracelet", "Elegant rose gold bangle with a modern twist", 120, 399.10, "2023-09-12"),
#     (6, "Cubic Zirconia Stud Earrings", "earrings", "Affordable and sparkling cubic zirconia stud earrings", 300, 49.10, "2023-09-12"),
#     (6, "Classic Leather Strap Watch", "watch", "A classic leather strap watch for everyday wear", 250, 99.10, "2023-09-12"),
#     (6, "Tanzanite Pendant Necklace", "necklace", "Exquisite tanzanite pendant necklace for a touch of color", 80, 799.10, "2023-09-12"),
#     (6, "Platinum Wedding Band", "ring", "Durable and elegant platinum wedding band for couples", 50, 999.10, "2023-09-12"),
#     (6, "Sapphire Tennis Bracelet", "bracelet", "A stunning sapphire tennis bracelet for a special gift", 90, 1499.10, "2023-09-12"),
#     (6, "Chronograph Pilot Watch", "watch", "A precision chronograph pilot watch for aviation enthusiasts", 100, 899.10, "2023-09-12"),
#     (6, "Ruby and Diamond Ring", "ring", "A captivating ruby and diamond ring for a romantic gift", 70, 1999.10, "2023-09-12"),
#     (6, "Cultured Pearl Necklace", "necklace", "Cultured pearl necklace with a timeless and elegant design", 110, 299.10, "2023-09-12"),
#     (6, "Gold Link Chain Bracelet", "bracelet", "Stylish gold link chain bracelet for a fashionable look", 130, 799.10, "2023-09-12"),
#     (6, "Diver's Stainless Steel Watch", "watch", "A rugged diver's stainless steel watch for water enthusiasts", 80, 599.10, "2023-09-12"),
#     (6, "Aquamarine and Diamond Earrings", "earrings", "Gorgeous aquamarine and diamond earrings for a special occasion", 50, 1799.10, "2023-09-12"),
#     (6, "Platinum Solitaire Ring", "ring", "A timeless platinum solitaire ring with a brilliant diamond", 40, 3499.10, "2023-09-12"),
#         (7, "Sofa Set with Coffee Table", "sofa_set", "Elegant sofa set with a matching coffee table for your living room", 50, 799.10, "2023-09-12"),
#     (7, "Queen Size Platform Bed", "bed", "A comfortable queen size platform bed with a modern design", 100, 499.10, "2023-09-12"),
#     (7, "Stainless Steel Refrigerator", "refrigerator", "Spacious stainless steel refrigerator with advanced cooling features", 80, 1099.10, "2023-09-12"),
#     (7, "Smart Thermostat", "thermostat", "Efficiently control your home's temperature with a smart thermostat", 200, 129.10, "2023-09-12"),
#     (7, "Front Load Washing Machine", "washing_machine", "High-capacity front load washing machine for your laundry needs", 70, 799.10, "2023-09-12"),
#     (7, "Cordless Vacuum Cleaner", "vacuum_cleaner", "Convenient cordless vacuum cleaner for easy cleaning around the house", 150, 199.10, "2023-09-12"),
#     (7, "Leather Recliner Chair", "chair", "Luxurious leather recliner chair for relaxation and comfort", 70, 599.10, "2023-09-12"),
#     (7, "Air Purifier with HEPA Filter", "air_purifier", "Improve indoor air quality with an air purifier featuring a HEPA filter", 120, 149.10, "2023-09-12"),
#     (7, "LED Ceiling Fan with Remote", "ceiling_fan", "Stay cool and save energy with an LED ceiling fan controlled by a remote", 90, 129.10, "2023-09-12"),
#     (7, "Electric Coffee Maker", "coffee_maker", "Brew your favorite coffee with an electric coffee maker", 200, 39.10, "2023-09-12"),
#     (7, "Sectional Corner Sofa", "sofa", "Modular sectional corner sofa for flexible seating arrangements", 50, 899.10, "2023-09-12"),
#     (7, "Memory Foam Mattress", "mattress", "High-quality memory foam mattress for a good night's sleep", 80, 399.10, "2023-09-12"),
#     (7, "Microwave Oven", "microwave_oven", "Convenient microwave oven for quick and easy cooking", 100, 79.10, "2023-09-12"),
#     (7, "Robotic Vacuum Cleaner", "robotic_vacuum", "Effortless cleaning with a robotic vacuum cleaner that does the work for you", 70, 249.10, "2023-09-12"),
#     (7, "5-Piece Dining Set", "dining_set", "Complete dining set with a table and four chairs for family meals", 40, 499.10, "2023-09-12"),
#     (7, "Smart Doorbell Camera", "doorbell_camera", "Enhance home security with a smart doorbell camera", 120, 199.10, "2023-09-12"),
#     (7, "Blender with Multiple Speeds", "blender", "Versatile blender with multiple speed settings for blending and mixing", 150, 79.10, "2023-09-12"),
#     (7, "L-shaped Computer Desk", "desk", "Functional L-shaped computer desk for your home office setup", 80, 249.10, "2023-09-12"),
#     (7, "Rice Cooker with Steamer", "rice_cooker", "Cook perfect rice and steam your favorite dishes with a rice cooker", 100, 49.10, "2023-09-12"),
#     (7, "Electric Fireplace Heater", "fireplace_heater", "Stay warm and cozy with an electric fireplace heater", 70, 299.10, "2023-09-12"),
#      (8, "Leather Tote Bag", "bag", "Elegant leather tote bag for everyday use or special occasions", 100, 199.10, "2023-09-12"),
#     (8, "Running Shoes", "shoes", "Comfortable and supportive running shoes for your active lifestyle", 200, 79.10, "2023-09-12"),
#     (8, "Canvas Backpack", "bag", "Durable canvas backpack with multiple compartments for storage", 150, 49.10, "2023-09-12"),
#     (8, "High Heel Pumps", "shoes", "Stylish high heel pumps for a fashionable look", 80, 89.10, "2023-09-12"),
#     (8, "Crossbody Bag", "bag", "Versatile crossbody bag with an adjustable strap for convenience", 120, 59.10, "2023-09-12"),
#     (8, "Sneakers", "shoes", "Classic sneakers for a casual and comfortable style", 250, 79.10, "2023-09-12"),
#     (8, "Leather Briefcase", "bag", "Professional leather briefcase for carrying your work essentials", 70, 129.10, "2023-09-12"),
#     (8, "Ankle Boots", "shoes", "Trendy ankle boots for a chic and stylish look", 90, 109.10, "2023-09-12"),
#     (8, "Travel Duffel Bag", "bag", "Spacious travel duffel bag with a durable design for trips", 100, 79.10, "2023-09-12"),
#     (8, "Loafers", "shoes", "Classic loafers for a comfortable and timeless style", 120, 79.10, "2023-09-12"),
#     (8, "Shoulder Bag", "bag", "Stylish shoulder bag with a trendy design for everyday use", 150, 49.10, "2023-09-12"),
#     (8, "Men's Dress Shoes", "shoes", "Sophisticated men's dress shoes for formal occasions", 80, 99.10, "2023-09-12"),
#     (8, "Backpack with Laptop Compartment", "bag", "Functional backpack with a dedicated laptop compartment for work or school", 100, 79.10, "2023-09-12"),
#     (8, "Platform Sandals", "shoes", "Trendy platform sandals for a fashionable summer look", 120, 59.10, "2023-09-12"),
#     (8, "Leather Clutch", "bag", "Elegant leather clutch for special evenings or events", 70, 39.10, "2023-09-12"),
#     (8, "Hiking Boots", "shoes", "Durable hiking boots for outdoor adventures and trails", 70, 119.10, "2023-09-12"),
#     (8, "Weekender Bag", "bag", "Spacious weekender bag for short getaways and trips", 80, 89.10, "2023-09-12"),
#     (8, "Espadrille Wedges", "shoes", "Comfortable espadrille wedges for a stylish summer look", 100, 49.10, "2023-09-12"),
#     (8, "Leather Satchel", "bag", "Classic leather satchel for a timeless and sophisticated style", 70, 79.10, "2023-09-12"),
#     (8, "Running Sneakers", "shoes", "Performance-oriented running sneakers for athletes and runners", 100, 99.10, "2023-09-12"),
#     (9, "Plush Teddy Bear", "toy", "Soft and cuddly plush teddy bear for kids to snuggle with", 200, 19.10, "2023-09-12"),
#     (9, "Wooden Building Blocks", "toy", "Colorful wooden building blocks for creative play and learning", 150, 29.10, "2023-09-12"),
#     (9, "Baby Stroller with Canopy", "stroller", "Comfortable baby stroller with a protective canopy for outdoor walks", 100, 99.10, "2023-09-12"),
#     (9, "Educational Alphabet Puzzle", "puzzle", "Interactive alphabet puzzle for teaching letters and words to toddlers", 120, 14.10, "2023-09-12"),
#     (9, "Kids' Art Supplies Set", "art_supplies", "Complete art supplies set for young artists to explore their creativity", 180, 24.10, "2023-09-12"),
#     (9, "Baby Onesies Pack", "clothing", "Adorable pack of baby onesies in various cute designs", 250, 19.10, "2023-09-12"),
#     (9, "Remote Control Toy Car", "toy_car", "Fun remote control toy car for kids to race and play with", 100, 39.10, "2023-09-12"),
#     (9, "Baby High Chair", "high_chair", "Sturdy and adjustable baby high chair for mealtime convenience", 80, 59.10, "2023-09-12"),
#     (9, "Plastic Play Kitchen Set", "play_kitchen", "Interactive plastic play kitchen set for imaginative cooking adventures", 90, 49.10, "2023-09-12"),
#     (9, "Baby Diaper Bag Backpack", "diaper_bag", "Functional and stylish baby diaper bag backpack for parents on the go", 150, 34.10, "2023-09-12"),
#     (9, "Colorful Toy Blocks Set", "toy", "Vibrant and stackable toy blocks set for creative building", 200, 9.10, "2023-09-12"),
#     (9, "Kids' Bike with Training Wheels", "bike", "Durable kids' bike with training wheels for learning to ride", 70, 79.10, "2023-09-12"),
#     (9, "Baby Bath Tub", "bath_tub", "Comfortable and safe baby bath tub for bath time fun", 120, 19.10, "2023-09-12"),
#     (9, "Musical Baby Mobile", "mobile", "Musical baby mobile with cute plush animals to entertain and soothe", 100, 29.10, "2023-09-12"),
#     (9, "Outdoor Play Swing Set", "swing_set", "Outdoor play swing set for kids to enjoy swinging and playing outdoors", 80, 99.10, "2023-09-12"),
#     (9, "Baby Feeding Set", "feeding_set", "Convenient baby feeding set with utensils and plates for mealtime", 150, 14.10, "2023-09-12"),
#     (9, "Educational Learning Tablet", "tablet", "Interactive educational learning tablet for early childhood education", 180, 29.10, "2023-09-12"),
#     (9, "Kids' Inflatable Pool", "pool", "Fun and safe inflatable pool for kids to splash and play in the backyard", 100, 49.10, "2023-09-12"),
#     (9, "Baby Monitor with Camera", "baby_monitor", "Video baby monitor with camera for keeping an eye on your baby", 120, 79.10, "2023-09-12"),
#     (9, "Soft Plush Baby Blanket", "blanket", "Soft and cozy plush baby blanket for keeping your little one warm", 200, 17.10, "2023-09-12"),
#      (10, "Outdoor Camping Tent", "tent", "Spacious camping tent for outdoor adventures. Easy setup, weather-resistant.", 50, 199.10, "2023-09-12"),
#     (10, "Mountain Biking Adventure Package", "bike", "High-performance mountain bike package with safety gear. Ready for off-road excitement.", 30, 499.10, "2023-09-12"),
#     (10, "Camping Cookware Set", "cookware", "Portable cookware set for outdoor meals. Easy to use, heat-resistant materials.", 40, 79.10, "2023-09-12"),
#     (10, "Inflatable Stand-Up Paddleboard", "paddleboard", "Versatile inflatable paddleboard for water fun. Stable and perfect for workouts.", 50, 349.10, "2023-09-12"),
#     (10, "Premium Golf Club Set", "golf_club", "Comprehensive golf club set to enhance your game. Includes high-quality clubs.", 25, 799.10, "2023-09-12"),
#     (10, "Camping Hammock with Mosquito Net", "hammock", "Relaxing hammock with mosquito net for camping and lounging. Enjoy bug-free comfort.", 70, 59.10, "2023-09-12"),
#     (10, "Soccer Goal Set with Training Cones", "soccer_goal", "Soccer goal set with training cones for practice and matches. Fun for all ages.", 35, 129.10, "2023-09-12"),
#     (10, "Climbing Harness and Helmet Combo", "climbing_gear", "Safety harness and helmet for rock climbing. Comfortable and secure for adventurers.", 45, 139.10, "2023-09-12"),
#     (10, "Portable Disc Golf Set", "disc_golf", "Portable disc golf set for on-the-go fun. Precision discs suitable for all skill levels.", 40, 89.10, "2023-09-12"),
#     (10, "Adventure Camping Backpack", "backpack", "Rugged backpack for outdoor explorers. Spacious and weather-resistant design.", 30, 129.10, "2023-09-12"),
#     (10, "Basketball Hoop with Adjustable Height", "basketball_hoop", "Adjustable basketball hoop for outdoor fun. Suitable for players of all ages.", 50, 149.10, "2023-09-12"),
#     (10, "Outdoor Picnic Set for Family", "picnic_set", "Complete picnic set for family gatherings. Blanket, basket, and grill included.", 20, 179.10, "2023-09-12"),
#     (10, "Ultimate Frisbee Disc Set", "frisbee", "Ultimate Frisbee disc set for competitive play. High-quality discs for precise throws.", 35, 29.10, "2023-09-12"),
#     (10, "Camping Hammock with Rainfly", "hammock", "Hammock with built-in rainfly for camping comfort and weather protection.", 40, 79.10, "2023-09-12"),
#     (10, "Outdoor Yoga Mat with Carrying Bag", "yoga_mat", "Outdoor yoga mat for nature-inspired practice. Extra-thick and non-slip surface.", 50, 39.10, "2023-09-12"),
#     (10, "Adjustable Inline Skates", "skates", "Adjustable inline skates for all ages. Durable wheels for smooth rides.", 50, 59.10, "2023-09-12"),
#     (10, "Camping LED Lantern Set", "lantern", "Bright LED lanterns for outdoor illumination. Energy-efficient and water-resistant.", 70, 34.10, "2023-09-12"),
#     (10, "Family Badminton Set", "badminton_set", "Family badminton set for outdoor fun. Rackets, shuttlecocks, and net included.", 30, 49.10, "2023-09-12"),
#     (11, "Skin Renewal Serum", "serum", "Revitalize your skin with our Skin Renewal Serum. Reduces wrinkles and promotes youthful radiance.", 100, 39.10, "2023-09-12"),
#     (11, "Aromatherapy Essential Oils Set", "essential_oils", "Relax and rejuvenate with our Aromatherapy Essential Oils Set. Variety of fragrances for well-being.", 120, 29.10, "2023-09-12"),
#     (11, "Hair Growth Shampoo", "shampoo", "Achieve thicker, healthier hair with our Hair Growth Shampoo. Nourishes scalp and promotes growth.", 80, 19.10, "2023-09-12"),
#     (11, "Luxury Spa Robe", "robe", "Indulge in comfort with our Luxury Spa Robe. Plush and absorbent for a spa-like experience at home.", 150, 49.10, "2023-09-12"),
#     (11, "Electric Toothbrush with UV Sanitizer", "toothbrush", "Maintain oral health with our Electric Toothbrush. UV sanitizer kills germs for a fresh smile.", 50, 39.10, "2023-09-12"),
#     (11, "Organic Tea Tree Oil Soap", "soap", "Gentle and cleansing Organic Tea Tree Oil Soap. Ideal for acne-prone skin and natural cleansing.", 100, 9.10, "2023-09-12"),
#     (11, "Facial Cleansing Brush", "cleansing_brush", "Deep cleanse your skin with our Facial Cleansing Brush. Removes impurities for a radiant complexion.", 90, 24.10, "2023-09-12"),
#     (11, "Massage Oil Set", "massage_oil", "Experience relaxation with our Massage Oil Set. Variety of soothing oils for massages and self-care.", 80, 19.10, "2023-09-12"),
#     (11, "Anti-Aging Eye Cream", "eye_cream", "Reduce fine lines with our Anti-Aging Eye Cream. Nourishes delicate skin for a youthful look.", 120, 29.10, "2023-09-12"),
#     (11, "Herbal Hair Mask", "hair_mask", "Revive your hair with our Herbal Hair Mask. Deep conditioning for silky, shiny locks.", 100, 14.10, "2023-09-12"),
#     (11, "Natural Skin Toner", "toner", "Refresh your skin with our Natural Skin Toner. Restores pH balance and minimizes pores.", 80, 12.10, "2023-09-12"),
#     (11, "Electric Foot Spa Massager", "foot_massager", "Relieve tired feet with our Electric Foot Spa Massager. Soothes and rejuvenates for total relaxation.", 50, 49.10, "2023-09-12"),
#     (11, "Teeth Whitening Kit", "teeth_whitening_kit", "Achieve a brighter smile with our Teeth Whitening Kit. Safe and effective at-home whitening.", 90, 34.10, "2023-09-12"),
#     (11, "Silk Sleep Mask", "sleep_mask", "Improve sleep quality with our Silk Sleep Mask. Blocks out light for a restful night's sleep.", 120, 9.10, "2023-09-12"),
#     (11, "Collagen Peptide Powder", "collagen_powder", "Boost skin and joint health with our Collagen Peptide Powder. Supports youthful vitality.", 100, 29.10, "2023-09-12"),
#     (11, "Manicure and Pedicure Set", "manicure_set", "Nail care made easy with our Manicure and Pedicure Set. Professional grooming at home.", 150, 19.10, "2023-09-12"),
#     (11, "Moisturizing Hand Cream", "hand_cream", "Hydrate and soften hands with our Moisturizing Hand Cream. Non-greasy formula for smooth skin.", 80, 7.10, "2023-09-12"),
#     (11, "Lavender Bath Bombs", "bath_bombs", "Relaxing Lavender Bath Bombs for a spa-like bath experience. Soothes the senses and skin.", 90, 14.10, "2023-09-12"),
#     (11, "Essential Oil Diffuser", "diffuser", "Create a calming atmosphere with our Essential Oil Diffuser. Ultrasonic technology for aromatherapy.", 100, 29.10, "2023-09-12"),
#     (11, "Hair Styling Heat Protectant", "heat_protectant", "Protect hair from heat damage with our Hair Styling Heat Protectant. Shields and adds shine.", 50, 12.10, "2023-09-12"),
#     (12, "Compact Car Cover", "car_cover", "Protect your compact car from the elements with our durable car cover. Weather-resistant and UV protection.", 50, 49.10, "2023-09-12"),
#     (12, "Motorcycle Helmet", "helmet", "Stay safe on the road with our Motorcycle Helmet. DOT-certified for maximum protection.", 100, 59.10, "2023-09-12"),
#     (12, "Car Battery Charger", "battery_charger", "Keep your car battery charged with our Car Battery Charger. Easy to use and reliable.", 80, 34.10, "2023-09-12"),
#     (12, "Motorcycle Gloves", "gloves", "Protect your hands during rides with our Motorcycle Gloves. Comfortable and durable.", 120, 19.10, "2023-09-12"),
#     (12, "Car Floor Mats", "floor_mats", "Upgrade your car's interior with our Car Floor Mats. Stylish and easy to clean.", 150, 29.10, "2023-09-12"),
#     (12, "Motorcycle Chain Lubricant", "chain_lubricant", "Extend the life of your motorcycle chain with our Chain Lubricant. Superior protection and smooth rides.", 50, 12.10, "2023-09-12"),
#     (12, "Car Wash Kit", "car_wash_kit", "Maintain your car's shine with our Car Wash Kit. Complete set for a thorough clean.", 90, 24.10, "2023-09-12"),
#     (12, "Motorcycle Cover", "motorcycle_cover", "Protect your motorcycle from the elements with our Motorcycle Cover. Waterproof and durable.", 80, 39.10, "2023-09-12"),
#     (12, "Car Air Freshener", "air_freshener", "Keep your car smelling fresh with our Car Air Freshener. Various scents available.", 120, 7.10, "2023-09-12"),
#     (12, "Motorcycle Oil Filter", "oil_filter", "Maintain your motorcycle's engine with our Oil Filter. High-quality filtration for optimal performance.", 100, 9.10, "2023-09-12"),
#     (12, "Car Engine Oil", "engine_oil", "Keep your car's engine running smoothly with our Car Engine Oil. High-performance formula.", 150, 29.10, "2023-09-12"),
#     (12, "Motorcycle Brake Pads", "brake_pads", "Ensure safe braking with our Motorcycle Brake Pads. Designed for maximum stopping power.", 70, 14.10, "2023-09-12"),
#     (12, "Car Emergency Kit", "emergency_kit", "Be prepared on the road with our Car Emergency Kit. Includes essential tools and supplies.", 90, 49.10, "2023-09-12"),
#     (12, "Motorcycle Protective Jacket", "protective_jacket", "Stay protected during rides with our Motorcycle Protective Jacket. Armor and ventilation for comfort.", 50, 79.10, "2023-09-12"),
#     (12, "Car Wheel Locks", "wheel_locks", "Secure your car with our Car Wheel Locks. Deters theft and provides peace of mind.", 100, 19.10, "2023-09-12"),
#     (12, "Motorcycle Toolkit", "toolkit", "Perform maintenance on your motorcycle with our Motorcycle Toolkit. All the essential tools in one.", 80, 39.10, "2023-09-12"),
#     (12, "Car GPS Navigation System", "gps_system", "Never get lost with our Car GPS Navigation System. Reliable and easy-to-use navigation.", 120, 149.10, "2023-09-12"),
#     (12, "Motorcycle Riding Boots", "riding_boots", "Ride in style and safety with our Motorcycle Riding Boots. Durable and comfortable for long rides.", 90, 59.10, "2023-09-12"),
#     (12, "Car Seat Covers", "seat_covers", "Upgrade your car's seats with our Car Seat Covers. Custom-fit and stylish design.", 100, 39.10, "2023-09-12"),
#     (12, "Motorcycle Phone Mount", "phone_mount", "Stay connected on the road with our Motorcycle Phone Mount. Secure and adjustable.", 50, 14.10, "2023-09-12"),
#     (13, "Cordless Drill Kit", "drill", "Get the job done with our Cordless Drill Kit. Powerful and versatile for DIY projects.", 50, 89.10, "2023-09-12"),
#     (13, "Toolbox Set with Tools", "toolbox_set", "Organize your tools with our Toolbox Set. Complete with essential tools for repairs.", 50, 59.10, "2023-09-12"),
#     (13, "Paint Sprayer Kit", "paint_sprayer", "Achieve professional paint results with our Paint Sprayer Kit. Ideal for home improvement.", 40, 74.10, "2023-09-12"),
#     (13, "Safety Goggles", "safety_goggles", "Protect your eyes during work with our Safety Goggles. Comfortable and reliable eye protection.", 80, 9.10, "2023-09-12"),
#     (13, "Screwdriver Set", "screwdriver_set", "Complete your toolkit with our Screwdriver Set. Variety of sizes for various tasks.", 100, 14.10, "2023-09-12"),
#     (13, "Electric Angle Grinder", "angle_grinder", "Grind and cut with precision using our Electric Angle Grinder. Powerful and efficient.", 50, 49.10, "2023-09-12"),
#     (13, "Tool Belt with Pockets", "tool_belt", "Stay organized on the job with our Tool Belt. Multiple pockets for easy tool access.", 80, 19.10, "2023-09-12"),
#     (13, "Digital Multimeter", "multimeter", "Measure with accuracy using our Digital Multimeter. Ideal for electrical diagnostics.", 70, 24.10, "2023-09-12"),
#     (13, "Paint Roller Set", "paint_roller_set", "Paint with ease using our Paint Roller Set. Includes rollers, trays, and brushes.", 90, 19.10, "2023-09-12"),
#     (13, "Adjustable Wrench", "wrench", "Tighten and loosen with precision using our Adjustable Wrench. Durable and versatile.", 120, 12.10, "2023-09-12"),
#     (13, "Soldering Iron Kit", "soldering_kit", "Master soldering projects with our Soldering Iron Kit. Complete set for soldering tasks.", 50, 29.10, "2023-09-12"),
#     (13, "Power Saw with Laser Guide", "power_saw", "Make precise cuts with our Power Saw. Laser guide for accuracy in woodworking.", 40, 119.10, "2023-09-12"),
#     (13, "Safety Ear Muffs", "ear_muffs", "Protect your hearing with our Safety Ear Muffs. Comfortable and effective noise reduction.", 80, 14.10, "2023-09-12"),
#     (13, "Utility Knife Set", "utility_knife_set", "Cut materials with ease using our Utility Knife Set. Sharp blades and ergonomic design.", 100, 9.10, "2023-09-12"),
#     (13, "Digital Caliper", "caliper", "Measure accurately with our Digital Caliper. Ideal for precision measurements in DIY projects.", 50, 19.10, "2023-09-12"),
#     (13, "Carpenter's Square", "carpenters_square", "Ensure accurate angles with our Carpenter's Square. Essential for woodworking.", 90, 7.10, "2023-09-12"),
#     (13, "Pipe Wrench", "pipe_wrench", "Securely grip pipes with our Pipe Wrench. Durable construction for plumbing tasks.", 70, 29.10, "2023-09-12"),
#     (13, "Caulking Gun Set", "caulking_gun", "Apply sealants with precision using our Caulking Gun Set. Includes various tips for different jobs.", 50, 14.10, "2023-09-12"),
#     (13, "Adjustable Hacksaw", "hacksaw", "Cut through materials effortlessly with our Adjustable Hacksaw. Versatile and reliable.", 50, 12.10, "2023-09-12"),
#     (13, "Plumbing Snake", "plumbing_snake", "Clear clogged drains with ease using our Plumbing Snake. Effective and durable.", 80, 24.10, "2023-09-12")
# ]

# # You can insert this data into your database using SQLAlchemy
# for item in data:
#     product = Product(
#         category_id=item[0],
#         name=item[1],
#         type=item[2],
#         description=item[3],
#         stock=item[4],
#         price=item[5],
#         date=datetime.strptime(item[6], "%Y-%m-%d")  # Convert date string to datetime
#     )
#     session.add(product)

# session.commit()
# print('Products added successfully')
