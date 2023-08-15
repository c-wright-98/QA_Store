from app import app,db, Products, Category, Cart, Orders, User

indoors = Category(
    category_id = 101,
    name = 'Indoors'
)

outdoors = Category(
    category_id = 102,
    name = 'Outdoors'
)

indoors = Category(
    category_id = 103,
    name = 'Pot'
)

test_product = Products(
    product_id = 1001,
    category_id = 101,
    image_URL = 'static/images/plants/test-plant.png',
    description = 'This is a test',
    name = 'Test Product',
    price = 9.99,
    stock = 99
)

with app.app_context():
    db.create_all()