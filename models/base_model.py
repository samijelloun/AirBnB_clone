#!/usr/bin/python3
"""This module that represent classe BasseModel"""
import uuid
import datetime
import models


class BaseModel:
    """ This class of base model """

    def __init__(self, *args, **kwargs):
        """ Initialize BaseModel instance """
        if kwargs:
            for k, w in kwargs.items():
                if k == '__class__':
                    continue
                elif k in ['created_at', 'updated_at']:
                    w = datetime.datetime.now().fromisoformat(w)
                setattr(self, k, w)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ This method defines as a string """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """ This method represent updates the public instance attribute """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """This method represent a dictionary containing """
        obj_dict = self.__dict__.copy()
        obj_dict['id'] = self.id
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
