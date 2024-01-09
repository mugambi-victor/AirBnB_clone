#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """
    A base model with common attributes and methods for other classes.

    Public instance attributes:
    - id (str): Unique identifier assigned with a
    UUID when an instance is created.
    - created_at (datetime): Timestamp for the instance creation.
    - updated_at (datetime): Timestamp for the last update.

    Public instance methods:
    - save(): Updates the 'updated_at'
    attribute with the current datetime.
    - to_dict(): Returns a dictionary containing
    serialized representation of the instance.
    - __str__(): Returns a string representation of the instance.
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing serialized
        representation of the instance.

        Returns:
            dict: A dictionary containing instance
            attributes in a serialized format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns:
            str: A string representation of the instance.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )
