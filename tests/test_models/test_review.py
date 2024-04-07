#!/usr/bin/python3
"""Unittest for review"""
import unittest
from models.review import Review
from models.place import Place
from models.user import User


class TestReview(unittest.TestCase):
    """Unittest for Review class"""

    def test_save(self):
        """Test save method"""
        review = Review()
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)

    def test_str(self):
        """Test __str__ method"""
        review = Review()
        review.save()
        self.assertEqual(str(review), "[Review] ({}) {}".format(
            review.id, review.__dict__))

    def test_attribute_defaults(self):
        """Test default attribute values"""
        new_review = Review()
        self.assertEqual(new_review.place_id, "")
        self.assertEqual(new_review.user_id, "")
        self.assertEqual(new_review.text, "")

    def test_initialization(self):
        """Test initialization with specific values"""
        place = Place()
        user = User()
        new_review = Review(place_id=place.id, user_id=user.id, text="Great place!")
        self.assertEqual(new_review.place_id, place.id)
        self.assertEqual(new_review.user_id, user.id)
        self.assertEqual(new_review.text, "Great place!")


if __name__ == '__main__':
    unittest.main()
