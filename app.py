from flask import Flask, render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_testing import TestCase
from flask_bcrypt import Bcrypt
import os
from wtforms import StringField, IntegerField, DateField, ValidationError
from wtforms.validators import DataRequired, Length, NumberRange, AnyOf

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SECRET_KEY'] = "12736453"

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

################################
# Create database tables #
class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, unique = True)
    name = db.Column(db.String(50), nullable=False)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, unique = True)
    username = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(250), unique = True)

class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True, unique = True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)
    image_URL = db.Column(db.String(255))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True, unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    quantity = db.Column(db.Integer)

class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'), nullable=False)
    address = db.Column(db.String(255))

################################

# Creating Validator Classes #

class PaymentForm(FlaskForm):
    cardholder_name = StringField(
        "Cardholder Name",
        validators=[DataRequired(), Length(min=2, max=30)]
        )
    cardnumber = IntegerField(
        "Card Number",
        validators=[DataRequired(), Length(min=16, max=16)]
        )

    expire = StringField(
        "Expire Date",
        validators=[DataRequired(), Length(min=7, max=7)]
        )
    SC = IntegerField(
        "Security Code (CVC)",
        validators=[DataRequired(), Length(min=3, max=4)]
        )

    def validate_cardholder_name(self,field):
        if len(field.data) < 2 or len(field.data) > 30:
            raise ValidationError("Please enter a valid Name")

    def validate_cardnumber(self,field):
        if len(str(field.data)) < 16:
            raise ValidationError("Please enter a valid card number")

    def validate_expire(self,field):
        if len(field.data) < 7:
            raise ValidationError("Please enter a valid expiry date")

    def validate_SC(self,field):
        if len(str(field.data)) < 3 or len(str(field.data)) > 4:
            raise ValidationError("Please enter a valid Name")



################################
# App Routes #

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

@app.route('/payment', methods=['POST'])
def payment():
    message = ""
    form = PaymentForm()

    if form.validate_on_submit():
        message = "Successful Payment!"
        return message

    return render_template('payment.html')

@app.route('/checkout', methods=['GET','POST'])
def checkout():
    return render_template('checkout.html')

@app.route('/success', methods=['GET','POST'])
def successful():
    return render_template('success.html')

################################
# Running App #

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)