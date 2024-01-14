#!/usr/bin/python3
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Unit tests for the Place class.
    """

    def test_inheritance(self):
        """
        Test that Place inherits from BaseModel.
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of the Place class.
        """
        place = Place()
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_default_values(self):
        """
        Test that attributes have default values.
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_initialization(self):
        """
        Test the initialization of Place with arguments.
        """
        place_data = {
            'id': 'test_id',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            'city_id': 'test_city_id',
            'user_id': 'test_user_id',
            'name': 'Test Place',
            'description': 'Test Description',
            'number_rooms': 3,
            'number_bathrooms': 2,
            'max_guest': 6,
            'price_by_night': 150,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'amenity_ids': ['amenity1', 'amenity2']
        }
        place = Place(**place_data)
        self.assertEqual(place.id, 'test_id')
        self.assertEqual(str(place.created_at), '2022-01-01 00:00:00')
        self.assertEqual(str(place.updated_at), '2022-01-02 00:00:00')
        self.assertEqual(place.city_id, 'test_city_id')
        self.assertEqual(place.user_id, 'test_user_id')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, 'Test Description')
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 150)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ['amenity1', 'amenity2'])


if __name__ == '__main__':
    unittest.main()
