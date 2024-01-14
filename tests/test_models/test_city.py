#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Unit tests for the City class.
    """

    def test_inheritance(self):
        """
        Test that City inherits from BaseModel.
        """
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of the City class.
        """
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_default_values(self):
        """
        Test that attributes have default values.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_initialization(self):
        """
        Test the initialization of City with arguments.
        """
        city_data = {
            'id': 'test_id',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            'state_id': 'test_state_id',
            'name': 'Test City'
        }
        city = City(**city_data)
        self.assertEqual(city.id, 'test_id')
        self.assertEqual(str(city.created_at), '2022-01-01 00:00:00')
        self.assertEqual(str(city.updated_at), '2022-01-02 00:00:00')
        self.assertEqual(city.state_id, 'test_state_id')
        self.assertEqual(city.name, 'Test City')


if __name__ == '__main__':
    unittest.main()
