#!/usr/bin/python3
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import os

"""
Unit tests for FileStorage class in file_storage module.
"""

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Create an instance of FileStorage for testing
        self.file_storage = FileStorage()

    def tearDown(self):
        # Clean up: remove the test file if it exists
        if os.path.exists(self.file_storage.get_file_path()):
            os.remove(self.file_storage.get_file_path())

    def test_all(self):
        # Test if all method returns a dictionary
        result = self.file_storage.all()
        self.assertIsInstance(result, dict)

    def test_new(self):
        # Test if new method adds an object to __objects
        obj = BaseModel()
        self.file_storage.new(obj)
        result = self.file_storage.all()
        self.assertIn(f'{obj.__class__.__name__}.{obj.id}', result)

    def test_save_reload(self):
        # Test if save and reload methods work together
        obj1 = BaseModel()
        obj2 = User()
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)

        # Save the objects to a file
        self.file_storage.save()

        # Clear __objects to simulate reloading
        self.file_storage._FileStorage__objects = {}

        # Reload the objects from the file
        self.file_storage.reload()

        # Check if the reloaded objects match the original ones
        result = self.file_storage.all()
        self.assertIn(f'{obj1.__class__.__name__}.{obj1.id}', result)
        self.assertIn(f'{obj2.__class__.__name__}.{obj2.id}', result)

    @patch('os.path.exists', return_value=False)
    def test_reload_no_file(self, mock_exists):
        # Test reload method when the file doesn't exist
        self.file_storage.reload()
        result = self.file_storage.all()
        self.assertEqual(result, {})


if __name__ == '__main__':
    unittest.main()
