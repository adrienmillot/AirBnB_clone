#!/usr/bin/python3
""" PlaceTest module """


from models.place import Place
import unittest


class PlaceTest(unittest.TestCase):
    """ PlaceTest class """

    def testClassDocumentation(self):
        """
            Class have documentation
        """
        self.assertGreater(len(Place.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Constructor have documentation
        """
        self.assertGreater(len(Place.__init__.__doc__), 0)
