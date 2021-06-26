#!/usr/bin/python3
""" UserTest module """


from models.user import User
import unittest


class UserTest(unittest.TestCase):
    """ UserTest class """

    def testClassDocumentation(self):
        """
            Class have documentation
        """
        self.assertGreater(len(User.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Constructor have documentation
        """
        self.assertGreater(len(User.__init__.__doc__), 0)
