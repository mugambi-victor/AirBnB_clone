#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Unit tests for the State class.
    """

    def test_inheritance(self):
        """
        Test that State inherits from BaseModel.
        """
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of the State class.
        """
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))

    def test_default_values(self):
        """
        Test that attributes have default values.
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_initialization(self):
        """
        Test the initialization of State with arguments.
        """
        state_data = {
            'id': 'test_id',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            'name': 'Test State'
        }
        state = State(**state_data)
        self.assertEqual(state.id, 'test_id')
        self.assertEqual(str(state.created_at), '2022-01-01 00:00:00')
        self.assertEqual(str(state.updated_at), '2022-01-02 00:00:00')
        self.assertEqual(state.name, 'Test State')


if __name__ == '__main__':
    unittest.main()
