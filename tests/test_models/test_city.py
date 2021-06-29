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

    def testConstructor(self):
        """
            Constructor test
        """
        c1 = City()
        c1.name = "Lille"
        c1.save()
        self.assertGreater(c1.updated_at, c1.created_at)
        self.assertDictEqual(
            c1.to_dict(),
            {
                'id': c1.id,
                'created_at': c1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'updated_at': c1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'name': "Lille",
                '__class__': 'City'
            }
        )

    def testNameType(self):
        """
            Check name attribute type
        """
        self.assertIsInstance(City().name, str)

    def testStateIdType(self):
        """
            Check state_id attribute type
        """
        self.assertIsInstance(City().state_id, str)
