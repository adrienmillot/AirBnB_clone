#!/usr/bin/python3
""" Base module """


from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """ Base class """
    id = None
    created_at = None
    updated_at = None

    def __init__(self, *prmArgs, **prmKwArgs):
        """
            Constructor
        """
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())

        if prmKwArgs:
            for key, value in prmKwArgs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                elif key != "__class__":
                    setattr(self, key, value)

        storage.new(self)

    def __str__(self):
        """
            Function that return a string representation of the object
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__
        )

    def save(self):
        """
            Function that updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            Function that returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        dict = {}

        for key, value in self.__dict__.items():
            if not value:
                continue
            if key == 'created_at' or key == 'updated_at':
                dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                dict[key] = value

        dict["__class__"] = self.__class__.__name__

        return dict
