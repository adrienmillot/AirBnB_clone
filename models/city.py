#!/usr/bin/python3
""" City module """


from models.base_model import BaseModel


class City(BaseModel):
    """ City class """

    state_id = ""
    name = ""

    def __init__(self, *prmArgs, **prmKwArgs):
        """
            Constructor
        """
        super().__init__(*prmArgs, **prmKwArgs)
