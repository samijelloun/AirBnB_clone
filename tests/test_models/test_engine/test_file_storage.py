#!/usr/bin/python3
"""Test of file Storage"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage  hello  check and got this"""

    def setUp(self):
        """Set up the test cases"""
        self.storage = FileStorage()
        setattr(self.storage, "_FileStorage__objects", {})
        self.file_path = models.storage._FileStorage__file_path
        self.instance = BaseModel()
        self.objs = models.storage._FileStorage__objects
        self.keyname = f"BaseModel.{self.instance.id}"

    def tearDown(self):
        """Clean up"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all_method_exists(self):
        """Test all method"""
        self.assertTrue(hasattr(models.storage, "all"))

    def test_new_method_exists(self):
        """Test new method exists"""
        self.assertTrue(hasattr(models.storage, "new"))

    def test_reload_method_exists(self):
        """Test reload method exists"""
        self.assertTrue(hasattr(models.storage, "reload"))

    def test_all_method_returns_dict(self):
        """Test all method return dict"""
        result = models.storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method_adds_to_objects(self):
        """Test new method add to objects"""
        obj = BaseModel()
        models.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, models.storage.all().keys())

    def test_save_method_saves_to_file(self):
        """Test save method saves to file"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        models.storage.new(my_model)
        models.storage.save()
        with open(self.file_path, "r") as data_file:
            saved_data = json.load(data_file)
        expected_data = {key: value.to_dict() for key,
                         value in self.objs.items()}
        self.assertEqual(saved_data, expected_data)


if __name__ == "__main__":
    unittest.main() 
