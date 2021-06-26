#!/usr/bin/python3
""" AmenityTest module """


from models.amenity import Amenity
import unittest


class AmenityTest(unittest.TestCase):
    """ AmenityTest class """

    def testClassDocumentation(self):
        """
            Class have documentation
        """
        self.assertGreater(len(Amenity.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Constructor have documentation
        """
        self.assertGreater(len(Amenity.__init__.__doc__), 0)
