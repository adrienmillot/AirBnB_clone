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

    def testConstructor(self):
        """
            Constructor test
        """
        s1 = State()
        s1.name = "Lille"
        s1.save()
        self.assertGreater(s1.updated_at, s1.created_at)
        self.assertDictEqual(
            s1.to_dict(),
            {
                'id': s1.id,
                'created_at': s1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'updated_at': s1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'name': "Lille",
                '__class__': 'State'
            }
        )

    def testNameType(self):
        """
            Check name attribute type
        """
        self.assertIsInstance(State().name, str)
