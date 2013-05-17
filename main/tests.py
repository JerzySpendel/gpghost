"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import unittest
from main.models import User
class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User(login="Yuras",email="jspendel@gmail.com",password="hehebum")
    def test_creating_user(self):
        self.assertEqual(self.user.login,"Yuras")
        self.assertEqual(self.user.email,"jspendel@gmail.com")
        self.assertEqual(self.user.password,"hehebum")

