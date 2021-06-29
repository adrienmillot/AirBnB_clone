#!/usr/bin/python3
""" Amenity module """


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class """

    name = ""

    def __init__(self, *prmArgs, **prmKwArgs):
        """
            Constructor
        """
        super().__init__(*prmArgs, **prmKwArgs)
