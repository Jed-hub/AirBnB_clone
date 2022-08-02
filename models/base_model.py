#!/usr/bin/env python3
"""
The base module
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Description: Defines all common attributes/methods
    for other classes

    Attributes:
        id: a string with an UUID when an instance is created
        created_at: assign with the current datetime
            when an instance is created
        updated_at: assign with the current datetime
            when an isntance is created and
            it will be updated every time the object changes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of the instances
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key in ('created_at', 'updated_at'):
                    value = datetime
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        prints the class name and it's content
        """
        return '[{0}] ({1}) {2}'.format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        class_dict = self.__dict__.copy()
        class_dict['__class__'] = self.__class__.__name__
        class_dict['created_at'] = self.created_at.isoformat()
        class_dict['updated_at'] = self.updated_at.isoformat()

        return class_dict
