#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
import os
import models
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.base_model import BaseModel
from console import HBNBCommand

"""
Unit tests for HBNBCommand class in console module.
"""


class TestConsoleCommands(unittest.TestCase):

    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def tearDown(self):
        # Reset the storage
        models.storage._FileStorage__objects = {}

    def test_show_command_with_missing_instance_id(self):
        with patch('builtins.input', return_value='show User'):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.hbnb_command.onecmd("show User")
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "** instance id missing **")

    def test_show_command_with_non_existing_instance(self):
        with patch('builtins.input', return_value='show User 123'):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.hbnb_command.onecmd("show User 123")
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "** no instance found **")

    def test_create_command(self):
        with patch('builtins.input', return_value='create User'):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.hbnb_command.onecmd("create User")
                user_id = mock_stdout.getvalue().strip()
                self.assertTrue(
                        models.storage._FileStorage__objects.
                        get("User.{}".format(user_id)))

    def test_destroy_command_with_valid_input(self):
        user = User()
        user_id = user.id
        models.storage._FileStorage__objects["User.{}".format(user_id)] = user

        with patch(
                'builtins.input',
                return_value='destroy User {}'.
                format(user_id)):
            with patch(
                    'sys.stdout',
                    new_callable=StringIO) as mock_stdout:
                self.hbnb_command.onecmd("destroy User {}".format(user_id))
                self.assertIsNone(
                        models.storage._FileStorage__objects.
                        get("User.{}".format(user_id))
                        )

    def test_destroy_command_with_missing_class_name(self):
        with patch('builtins.input', return_value='destroy'):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.hbnb_command.onecmd("destroy")
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "** class name missing **")

    def test_all_command(self):
        user1 = User()
        user2 = User()
        models.storage._FileStorage__objects[
                "User.{}".format(user1.id)] = user1
        models.storage._FileStorage__objects[
                "User.{}".format(user2.id)] = user2

        with patch('builtins.input', return_value='all User'):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.hbnb_command.onecmd("all User")
                output = mock_stdout.getvalue().strip()
                self.assertIn(str(user1), output)
                self.assertIn(str(user2), output)

    def test_all_command_with_non_existing_class(self):
        with patch('builtins.input', return_value='all NonExistingClass'):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.hbnb_command.onecmd("all NonExistingClass")
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "** class doesn't exist **")

    def test_update_command(self):
        user = User()
        user_id = user.id
        models.storage._FileStorage__objects["User.{}".format(user_id)] = user

        with patch(
                'builtins.input',
                return_value='update User {} name "John"'.
                format(user_id)):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.hbnb_command.onecmd(
                        'update User {} name "John"'.
                        format(user_id)
                        )
                updated_user = models.storage._FileStorage__objects.get("User.{}".format(user_id))

                # Remove double quotes from the actual value for comparison
                actual_name = getattr(updated_user, 'name', None)
                if actual_name is not None and isinstance(
                        actual_name, str) and actual_name.startswith('"') and actual_name.endswith('"'):
                    actual_name = actual_name[1:-1]

                self.assertEqual(actual_name, "John")

    def test_update_command_with_missing_class_name(self):
        with patch('builtins.input', return_value='update'):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.hbnb_command.onecmd("update")
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "** class name missing **")

    def test_count_command(self):
        user1 = User()
        user2 = User()
        models.storage._FileStorage__objects[
                "User.{}".format(user1.id)] = user1
        models.storage. _FileStorage__objects[
                "User.{}".format(user2.id)] = user2

        with patch('builtins.input', return_value='count User'):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.hbnb_command.onecmd("count User")
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "2")

    def test_count_command_with_non_existing_class(self):
        with patch('builtins.input', return_value='count NonExistingClass'):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.hbnb_command.onecmd("count NonExistingClass")
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "** class doesn't exist **")


if __name__ == '__main__':
    unittest.main()
