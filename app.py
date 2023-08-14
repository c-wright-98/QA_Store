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

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/orders', methods=['GET','POST'])
def order_history():
    return render_template('orders.html')

@app.route('/products', methods=['GET','POST'])
def products():
    return render_template('products.html')

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
    return render_template(successful)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)