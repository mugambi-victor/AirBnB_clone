#!/usr/bin/python3
import uuid
from datetime import datetime
# from models import storage


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

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        try:
                            # Try to parse with microseconds
                            setattr(self, key, datetime.strptime
                                    (value, '%Y-%m-%dT%H:%M:%S.%f'))
                        except ValueError:
                            # If parsing fails, try without microseconds
                            setattr(self, key, datetime.strptime
                                    (value, '%Y-%m-%dT%H:%M:%S'))
                    else:
                        setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def save(self):
        """ Updates the 'updated_at' attribute with the current datetime.
        Calls the 'save' method of the storage instance.
        """
        from models import storage
        self.updated_at = datetime.now()

        # If it's a new instance, add a call to the 'new' method on storage
        if self.id not in storage.all():
            storage.new(self)
        storage.save()

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
