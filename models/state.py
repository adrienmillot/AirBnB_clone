#!/usr/bin/python3
""" State module """


from models.base_model import BaseModel


class State(BaseModel):
    """ State class """

    name = ""

    def __init__(self, *prmArgs, **prmKwArgs):
        """
            Constructor
        """
        super().__init__(*prmArgs, **prmKwArgs)
