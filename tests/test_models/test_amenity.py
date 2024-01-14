#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Unit tests for the Amenity class.
    """

    def test_inheritance(self):
        """
        Test that Amenity inherits from BaseModel.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of the Amenity class.
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))

    def test_default_values(self):
        """
        Test that attributes have default values.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_initialization(self):
        """
        Test the initialization of Amenity with arguments.
        """
        amenity_data = {
            'id': 'test_id',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            'name': 'Test Amenity'
        }
        amenity = Amenity(**amenity_data)
        self.assertEqual(amenity.id, 'test_id')
        self.assertEqual(str(amenity.created_at), '2022-01-01 00:00:00')
        self.assertEqual(str(amenity.updated_at), '2022-01-02 00:00:00')
        self.assertEqual(amenity.name, 'Test Amenity')


if __name__ == '__main__':
    unittest.main()
