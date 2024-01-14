#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Unit tests for the User class.
    """

    def test_inheritance(self):
        """
        Test that User inherits from BaseModel.
        """
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of the User class.
        """
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_default_values(self):
        """
        Test that attributes have default values.
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_initialization(self):
        """
        Test the initialization of User with arguments.
        """
        user_data = {
            'id': 'test_id',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            'email': 'test@example.com',
            'password': 'test_password',
            'first_name': 'Test',
            'last_name': 'User'
        }
        user = User(**user_data)
        self.assertEqual(user.id, 'test_id')
        self.assertEqual(str(user.created_at), '2022-01-01 00:00:00')
        self.assertEqual(str(user.updated_at), '2022-01-02 00:00:00')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'test_password')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')


if __name__ == '__main__':
    unittest.main()
