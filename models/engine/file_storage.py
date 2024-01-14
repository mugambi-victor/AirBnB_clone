#!/usr/bin/python3
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    FileStorage class for serializing instances to a JSON
    file and deserializing JSON files to instances.

    Private class attributes:
    - __file_path: string - path to the JSON file (ex: file.json)
    - __objects: dictionary - empty but will store all objects
    by <class name>.id
    Public instance methods:
    - all(self): returns the dictionary __objects
    - new(self, obj): sets in __objects the obj with key <obj class name>.id
    - save(self): serializes __objects to the JSON file (path: __file_path)
    - reload(self): deserializes the JSON file to __object
    (only if the JSON file (__file_path) exists; otherwise, do nothing.
    If the file doesn’t exist, no exception should be raised)
    """

    __file_path = "file.json"
    __objects = {}
    def get_file_path(self):
        return self.__file_path

    def all(self, cls=None):
        """
        Returns a dictionary of all objects of a given class.
        If cls is None, returns all objects.
        """
        if cls is None:
            return self.__objects

        key_prefix = "{}.".format(cls.__name__)
        return {key: obj for key, obj in self.__objects.items() if key.startswith(key_prefix)}

    def new(self, obj):
        """
        Sets the given object in __objects with the key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(
                    {k: v.to_dict() for k, v in self.__objects.items()},
                    file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        Only performs the operation if the JSON file
        (__file_path) exists; otherwise, does nothing.
        If the file doesn’t exist, no exception should be raised.
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.__objects = {}
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = globals()[class_name]
                    self.__objects[key] = cls(**value)
        else:
             self.__objects = {}
