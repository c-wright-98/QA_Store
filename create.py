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

# Indoor Plants #

dwarf_monstera_product = Products(
    product_id=1001,
    category_id=101,
    image_URL='static/images/plants/indoor/dwarf_monstera.png',
    description='This is a small monstera for the desk',
    name='Dwarf Monstera',
    price=19.99,
    stock=50
)

jade_plant_product = Products(
    product_id=1002,
    category_id=101,
    image_URL='static/images/plants/indoor/jade_plant.png',
    description='This is a jade plant',
    name='Jade Plant',
    price=14.99,
    stock=30
)

snake_plant_product = Products(
    product_id=1003,
    category_id=101,
    image_URL='static/images/plants/indoor/snake_plant.png',
    description='This is a snake plant',
    name='Snake Plant',
    price=12.99,
    stock=25
)

small_fern_product = Products(
    product_id=1004,
    category_id=101,
    image_URL='static/images/plants/indoor/small_fern.png',
    description='This is a small fern',
    name='Small Fern',
    price=8.99,
    stock=40
)

two_pair_product = Products(
    product_id=1005,
    category_id=101,
    image_URL='static/images/plants/indoor/succulent_pair.png',
    description='This is a pair of succulents',
    name='Two Succulents',
    price=17.99,
    stock=20
)


# Outdoor Plants #

aloe_vera_product = Products(
    product_id=2001,
    category_id=102,
    image_URL='static/images/plants/outdoor/aloe_vera.png',
    description='This is an Aloe Vera plant',
    name='Aloe Vera',
    price=14.99,
    stock=30
)

fig_plant_product = Products(
    product_id=2002,
    category_id=102,
    image_URL='static/images/plants/outdoor/fig_plant.png',
    description='This is a fig plant',
    name='Fig Plant',
    price=19.99,
    stock=25
)

water_lily_product = Products(
    product_id=2003,
    category_id=102,
    image_URL='static/images/plants/outdoor/water_lily.png',
    description='This is a water lily',
    name='Water Lily',
    price=8.99,
    stock=40
)

pearl_beads_product = Products(
    product_id=2004,
    category_id=102,
    image_URL='static/images/plants/outdoor/pearl_beads.png',
    description='These are pearl beads',
    name='Hanging Pearl Beads',
    price=12.99,
    stock=20
)

b_leaf_product = Products(
    product_id=2005,
    category_id=102,
    image_URL='static/images/plants/outdoor/banana_leaf_plant.png',
    description='This is a banana leaf plant',
    name='Banana Leaf Plant',
    price=9.99,
    stock=50
)


# Pots #

grey_pot = Products(
    product_id = 3001,
    category_id = 103,
    image_URL = 'static/images/pots/pot_grey.png',
    description = 'This is a simple grey pot',
    name = 'Grey Pot',
    price = 9.99,
    stock = 99
)

pot_stand = Products(
    product_id = 3002,
    category_id = 103,
    image_URL = 'static/images/pots/pot_stand.png',
    description = 'Pot stand for big plants',
    name = 'Pot Stand',
    price = 20.00,
    stock = 15
)

cute_pot = Products(
    product_id = 3003,
    category_id = 103,
    image_URL = 'static/images/pots/cute_pot.png',
    description = 'This is a cute frog pot',
    name = 'Frog Pot',
    price = 2.99,
    stock = 35
)

assorted_pots = Products(
    product_id = 3004,
    category_id = 103,
    image_URL = 'static/images/pots/assorted_pots.jpeg',
    description = 'This is three assorted pastel pots',
    name = '3x Pots',
    price = 9.99,
    stock = 67
)


with app.app_context():
    db.drop_all()
    db.create_all()

    db.session.add(indoors)
    db.session.add(outdoors)
    db.session.add(pots)

    db.session.add(dwarf_monstera_product)
    db.session.add(jade_plant_product)
    db.session.add(snake_plant_product)
    db.session.add(small_fern_product)
    db.session.add(two_pair_product)

    db.session.add(aloe_vera_product)
    db.session.add(fig_plant_product)
    db.session.add(water_lily_product)
    db.session.add(pearl_beads_product)
    db.session.add(b_leaf_product)

    db.session.add(grey_pot)
    db.session.add(pot_stand)
    db.session.add(cute_pot)
    db.session.add(assorted_pots)

    db.session.commit()