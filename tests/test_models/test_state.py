#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        """Set up for testing"""
        self.test_state = State()

    def test_instance(self):
        """Test if the object is an instance of State"""
        self.assertIsInstance(self.test_state, State)

    def test_attributes(self):
        """Test if the attributes are present"""
        self.assertTrue(hasattr(self.test_state, 'name'))

    def test_attributes_default_value(self):
        """Test if the attributes have default values"""
        self.assertEqual(self.test_state.name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        state_dict = self.test_state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_str(self):
        """Test __str__ method"""
        expected_str = "[State] ({}) {}".format(
            self.test_state.id, self.test_state.__dict__)
        self.assertEqual(str(self.test_state), expected_str)


if __name__ == '__main__':
    unittest.main()
