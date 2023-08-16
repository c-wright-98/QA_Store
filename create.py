from app import app,db, Products, Category, Cart, Orders, User

indoors = Category(
    category_id = 101,
    name = 'Indoors'
)

outdoors = Category(
    category_id = 102,
    name = 'Outdoors'
)

pots = Category(
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

test_product2 = Products(
    product_id = 1002,
    category_id = 102,
    image_URL = 'static/images/plants/test-plant.png',
    description = 'This is a test',
    name = 'Test Product',
    price = 9.99,
    stock = 99
)

test_product3 = Products(
    product_id = 1003,
    category_id = 103,
    image_URL = 'static/images/plants/test-plant.png',
    description = 'This is a test',
    name = 'Test Product',
    price = 9.99,
    stock = 99
)


with app.app_context():
    db.create_all()
    db.session.add(indoors)
    db.session.add(outdoors)
    db.session.add(pots)
    db.session.add(test_product)
    db.session.add(test_product2)
    db.session.add(test_product3)
    db.session.commit()