#!/usr/bin/python3
""" CityTest module """


from models.city import City
import unittest


class CityTest(unittest.TestCase):
    """ CityTest class """

    def testClassDocumentation(self):
        """
            Class have documentation
        """
        self.assertGreater(len(City.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Constructor have documentation
        """
        self.assertGreater(len(City.__init__.__doc__), 0)
