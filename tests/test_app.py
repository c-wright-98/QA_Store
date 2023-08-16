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

    def tearDown(self):
    # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

#def test_home_page():