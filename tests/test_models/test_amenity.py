#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittest for Amenity"""

    def test_str(self):
        """test str"""
        amenity = Amenity()
        amenity.save()
        self.assertEqual(str(amenity), "[Amenity] ({}) {}".format(
            amenity.id, amenity.__dict__))

    def test_name(self):
        """Test name"""
        amenity = Amenity()
        amenity.name = "Wifi"
        self.assertEqual(amenity.name, "Wifi")

    def test_id(self):
        """Test id"""
        amenity = Amenity()
        amenity.name = "Wifi"
        self.assertIsInstance(amenity.id, str)
        self.assertEqual(len(amenity.id), 36)

    def test_save(self):
        """test save"""
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

    def test_type_amenity(self):
        """test type amenity"""
        self.new_amenity = Amenity()
        self.assertEqual(self.new_amenity.name, "")

    def test_save(self):
        """test save"""
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
