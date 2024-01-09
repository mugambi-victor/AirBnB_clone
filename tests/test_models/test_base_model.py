#!/usr/bin/python3
import unittest
from Models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        instance = BaseModel()

        # Check if id is a valid UUID
        self.assertTrue(uuid.UUID(instance.id))


        # Check if created_at and updated_at are datetime objects
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

        # Check if created_at and updated_at are roughly equal (as they are initialized at the same time)
        self.assertAlmostEqual(instance.created_at.timestamp(), instance.updated_at.timestamp(), delta=0.01)


if __name__ == '__main__':
    unittest.main()
