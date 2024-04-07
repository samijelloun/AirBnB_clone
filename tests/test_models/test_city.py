#!/usr/bin/python3
"""Unittest for city"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_state_id_default_value(self):
        self.assertEqual(self.city.state_id, "")

    def test_name_default_value(self):
        self.assertEqual(self.city.name, "")

    def test_set_state_id(self):
        state_id = "123"
        self.city.state_id = state_id
        self.assertEqual(self.city.state_id, state_id)

    def test_set_name(self):
        name = "New York"
        self.city.name = name
        self.assertEqual(self.city.name, name)

if __name__ == '__main__':
    unittest.main()

