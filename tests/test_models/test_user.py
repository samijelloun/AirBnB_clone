#!/usr/bin/python3
"""Unittest for user"""
import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """Unittest for user"""

    def test_save(self):
        """test save"""
        user = User()
        user.save()
        self.assertNotEqual(user.created_at, user.updated_at)

    def test_str(self):
        """test str"""
        user = User()
        user.save()
        self.assertEqual(str(user), "[User] ({}) {}".format(
            user.id, user.__dict__))

    def test_type_user(self):
        """test type user"""
        self.new_user = User()
        self.assertEqual(self.new_user.email, "")
        self.assertEqual(self.new_user.password, "")
        self.assertEqual(self.new_user.first_name, "")
        self.assertEqual(self.new_user.last_name, "")


if __name__ == '__main__':
    unittest.main()
