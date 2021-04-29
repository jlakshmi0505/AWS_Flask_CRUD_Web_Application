import os, sys

import app
import db

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))
basedir = os.path.abspath(os.path.dirname(__file__))

import unittest
from models import Employee


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.db_uri = 'sqlite:///' + os.path.join(basedir, 'test.db')
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_models(self):
        # Create a customer user
        emp = Employee('b', 'b@gmail.com', 'USA', 'Google')
        db.session.add(emp)
        db.session.commit()

        # Create 2 consultant users
        user1 = Employee('b1', 'b1@gmail.com', 'USA', 'Google')
        db.session.add(user1)
        user2 = Employee('abc', 'abc@gmail.com', 'USA', 'Google')
        db.session.add(user2)
        db.session.commit()

        # Check that all users exist
        assert len(Employee.query.all()) is 3
