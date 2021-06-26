#!/usr/bin/python3
""" FileStorageTest module """


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import unittest


class FileStorageTest(unittest.TestCase):
    """ FileStorageTest class """

    def testClassDocumentation(self):
        """
            Class have documentation
        """
        self.assertGreater(len(FileStorage.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Constructor have documentation
        """
        self.assertGreater(len(FileStorage.__init__.__doc__), 0)

    def testAllDocumentation(self):
        """
            All have documentation
        """
        self.assertGreater(len(FileStorage.all.__doc__), 0)

    def testNewDocumentation(self):
        """
            New have documentation
        """
        self.assertGreater(len(FileStorage.new.__doc__), 0)

    def testSaveDocumentation(self):
        """
            Save have documentation
        """
        self.assertGreater(len(FileStorage.save.__doc__), 0)

    def testReloadDocumentation(self):
        """
            Reload have documentation
        """
        self.assertGreater(len(FileStorage.reload.__doc__), 0)

    def testAll(self):
        """
            Test all function
        """
        f1 = FileStorage()
        self.assertIsInstance(f1.all(), dict)

    def testNew(self):
        """
            Test new function
        """
        f1 = FileStorage()
        self.assertEqual(len(f1.all()), 4)
        b1 = BaseModel()
        f1.new(b1)
        self.assertEqual(len(f1.all()), 5)
        for key, value in f1.all().items():
            self.assertIsInstance(key, str)
            self.assertEqual(key, "{}.{}".format(
                type(value).__name__,
                value.id)
            )

    def testSave(self):
        """
            Test save function
        """
        f1 = FileStorage()
        f1.save()
        self.assertTrue(os.path.isfile("file.json"))
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def testReload(self):
        """
            Test reload function
        """
        f1 = FileStorage()
        f1.reload()
        self.assertEqual(len(f1.all()), 5)
        f1.save()
        if os.path.isfile("file.json"):
            os.remove("file.json")
