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

    def testEmailType(self):
        """
            Check email attribute type
        """
        self.assertIsInstance(User().email, str)

    def testPasswordType(self):
        """
            Check password attribute type
        """
        self.assertIsInstance(User().password, str)

    def testFirstNameType(self):
        """
            Check first_name attribute type
        """
        self.assertIsInstance(User().first_name, str)

    def testLastNameType(self):
        """
            Check last_name attribute type
        """
        self.assertIsInstance(User().last_name, str)
