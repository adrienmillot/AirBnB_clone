#!/usr/bin/python3
""" ReviewTest module """


from models.review import Review
import unittest


class ReviewTest(unittest.TestCase):
    """ ReviewTest class """

    def testClassDocumentation(self):
        """
            Class have documentation
        """
        self.assertGreater(len(Review.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Constructor have documentation
        """
        self.assertGreater(len(Review.__init__.__doc__), 0)

    def testConstructor(self):
        """
            Constructor test
        """
        r1 = Review()
        r1.text = "une petite review pour le fun"
        r1.save()
        self.assertGreater(r1.updated_at, r1.created_at)
        self.assertDictEqual(
            r1.to_dict(),
            {
                'id': r1.id,
                'created_at': r1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'updated_at': r1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'text': "une petite review pour le fun",
                '__class__': 'Review'
            }
        )

    def testPlaceIdType(self):
        """
            Check place_id type
        """
        self.assertIsInstance(Review().place_id, str)

    def testUserIdType(self):
        """
            Check user_id type
        """
        self.assertIsInstance(Review().user_id, str)

    def testTextType(self):
        """
            Check text type
        """
        self.assertIsInstance(Review().text, str)
