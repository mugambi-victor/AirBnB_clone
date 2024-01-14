#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Unit tests for the Review class.
    """

    def test_inheritance(self):
        """
        Test that Review inherits from BaseModel.
        """
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of the Review class.
        """
        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_default_values(self):
        """
        Test that attributes have default values.
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_initialization(self):
        """
        Test the initialization of Review with arguments.
        """
        review_data = {
            'id': 'test_id',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            'place_id': 'test_place_id',
            'user_id': 'test_user_id',
            'text': 'Test Review'
        }
        review = Review(**review_data)
        self.assertEqual(review.id, 'test_id')
        self.assertEqual(str(review.created_at), '2022-01-01 00:00:00')
        self.assertEqual(str(review.updated_at), '2022-01-02 00:00:00')
        self.assertEqual(review.place_id, 'test_place_id')
        self.assertEqual(review.user_id, 'test_user_id')
        self.assertEqual(review.text, 'Test Review')


if __name__ == '__main__':
    unittest.main()
