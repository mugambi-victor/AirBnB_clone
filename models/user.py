#!/usr/bin/python3
"""
This module holds the contens of the class User.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User Inherits BaseModel
        Public class attributes:
            * email -> String, Empty string
            * password -> String, Empty String
            * first_name -> String, Empty String
            * last_name -> String, Empty String
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Uses the super class for instatnsiation
        """
        super().__init__(*args, **kwargs)
