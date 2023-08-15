from flask import Flask, render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_testing import TestCase
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SECRET_KEY'] = "12736453"

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

################################################################
# Create database tables #
class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(250), unique = True)

class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    quantity = db.Column(db.Integer)

class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'), nullable=False)
    address = db.Column(db.String(255))

################################

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/orders', methods=['GET','POST'])
def order_history():
    return render_template('orders.html')

@app.route('/products', methods=['GET','POST'])
def products():
    products = Products.query.all()
    return render_template('products.html', products=products)

@app.route('/categories', methods=['GET','POST'])
def categories():
    return render_template('categories.html')

@app.route('/cart', methods=['GET','POST'])
def cart():
    return render_template('cart.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route('/contact-us', methods=['GET','POST'])
def contact():
    return render_template('contact.html')

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/payment', methods=['GET','POST'])
def payment():
    return render_template('payment.html')

@app.route('/checkout', methods=['GET','POST'])
def checkout():
    return render_template('checkout.html')

@app.route('/success', methods=['GET','POST'])
def successful():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)