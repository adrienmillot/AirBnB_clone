#!/usr/bin/python3
""" StateTest module """


from models.state import State
import unittest


class StateTest(unittest.TestCase):
    """ StateTest class """

    def testClassDocumentation(self):
        """
            Class have documentation
        """
        self.assertGreater(len(State.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Constructor have documentation
        """
        self.assertGreater(len(State.__init__.__doc__), 0)
