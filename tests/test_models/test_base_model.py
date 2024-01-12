#!/usr/bin/python3
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
import uuid
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        # Create an instance of BaseModel for testing
        self.obj = BaseModel()

    def test_init(self):
        instance = BaseModel()

        # Check if id is a valid UUID
        self.assertTrue(uuid.UUID(instance.id))


        # Check if created_at and updated_at are datetime objects
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

        # Check if created_at and updated_at are roughly equal (as they are initialized at the same time)
        self.assertAlmostEqual(instance.created_at.timestamp(), instance.updated_at.timestamp(), delta=0.01)
    @patch('models.base_model.datetime')
    def test_save_updates_updated_at(self, mock_datetime):
        # Mock current datetime to control the test
        mock_datetime.now.return_value = datetime(2024, 1, 8, 12, 0, 0)

        # Create an instance of BaseModel
        base_model = BaseModel()

        # Set specific values for testing
        base_model.updated_at = datetime(2023, 1, 8, 12, 0, 0)

        # Call save() method
        base_model.save()

        # Assert that the updated_at attribute has been updated
        expected_updated_at = datetime(2024, 1, 8, 12, 0, 0)
        self.assertEqual(base_model.updated_at, expected_updated_at)
    def test_to_dict(self):
        # Call the to_dict method and check the returned dictionary
        result_dict = self.obj.to_dict()

        # Assertions to check the content of the dictionary
        self.assertIsInstance(result_dict, dict)
        self.assertEqual(result_dict['__class__'], 'BaseModel')
        self.assertEqual(result_dict['created_at'], self.obj.created_at.isoformat())
        self.assertEqual(result_dict['updated_at'], self.obj.updated_at.isoformat())
    def test_str(self):
        # Call the __str__ method and check if it returns a string
        result_str = str(self.obj)
        self.assertIsInstance(result_str, str)

if __name__ == '__main__':
    unittest.main()
