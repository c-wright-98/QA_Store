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

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the home page"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)