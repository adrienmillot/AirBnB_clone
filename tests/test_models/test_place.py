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

    def testConstructor(self):
        """
            Constructor test
        """
        p1 = Place()
        p1.name = "Lille"
        p1.description = "Petite description de test"
        p1.number_rooms = 5
        p1.number_bathrooms = 1
        p1.max_guest = 4
        p1.price_by_night = 30
        p1.latitude = 32.56
        p1.longitude = 78.12
        p1.save()
        self.assertGreater(p1.updated_at, p1.created_at)
        self.assertDictEqual(
            p1.to_dict(),
            {
                'id': p1.id,
                'created_at': p1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'updated_at': p1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'name': "Lille",
                'description': 'Petite description de test',
                'number_rooms': 5,
                'number_bathrooms': 1,
                'max_guest': 4,
                'price_by_night': 30,
                'latitude': 32.56,
                'longitude': 78.12,
                '__class__': 'Place'
            }
        )
