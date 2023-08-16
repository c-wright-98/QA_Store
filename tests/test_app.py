import pytest
from app import app,db,Products,Orders,User,Cart,Category
from flask_testing import TestCase
from flask import url_for


class TestBase(TestCase):
        def create_app(self):
        # Pass in testing configurations for the app.
        # Here we use sqlite without a persistent database for our tests.
            app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                    SECRET_KEY='TEST_SECRET_KEY',
                    DEBUG=True,
                    WTF_CSRF_ENABLED=False
                    )
            return app

class TestViews(TestBase):

    def test_products_page(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_cart_page(self):
        response = self.app.get('/cart')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_payment_page(self):
        response = self.app.get('/payment')
        self.assertEqual(response.status_code, 200)