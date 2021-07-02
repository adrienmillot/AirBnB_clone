#!/usr/bin/python3
""" FileStorageTest module """


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models import storage
import unittest


class FileStorageAllTest(unittest.TestCase):
    def testAllInstance(self):
        storage = FileStorage()
        newDict = storage.all()
        self.assertIsInstance(newDict, dict)
        self.assertDictEqual(newDict, FileStorage._FileStorage__objects)


class FileStorageNewTest(unittest.TestCase):
    __classes = {
        'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
        'Amenity': Amenity, 'Place': Place, 'Review': Review
    }

    def testNewInstance(self):
        """
            new() function test
        """
        for classNameStr, className in self.__classes.items():
            self.__newInstance(classNameStr, className)

    def __newInstance(self, prmClassNameStr, prmClassName):
        tmpDict = storage.all()
        instance = prmClassName()
        key = "{}.{}".format(prmClassNameStr, instance.id)
        self.assertDictEqual(tmpDict, storage.all())
        storage.new(instance)
        tmpDict[key] = instance
        self.assertDictEqual(tmpDict, storage.all())


class FileStorageSaveTest(unittest.TestCase):
    __classes = {
        'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
        'Amenity': Amenity, 'Place': Place, 'Review': Review
    }

    def testSaveInstance(self):
        """
            save() function test
        """
        for classNameStr, className in self.__classes.items():
            self.__saveInstance(classNameStr, className)

    def __saveInstance(self, prmClassNameStr, prmClassName):
        import json

        tmpDict = {}
        for key, value in storage.all().items():
            tmpDict[key] = value.to_dict()
        instance = prmClassName()
        key = "{}.{}".format(prmClassNameStr, instance.id)
        storage.new(instance)
        storage.save()
        tmpDict[key] = instance.to_dict()
        inputStr = json.dumps(tmpDict)
        with open("file.json", "r") as file:
            output = file.read()
        self.assertEqual(json.loads(inputStr), json.loads(output))


class FileStorageReloadTest(unittest.TestCase):
    __classes = {
        'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
        'Amenity': Amenity, 'Place': Place, 'Review': Review
    }

    def testReloadInstance(self):
        """
            reload() function test
        """
        for classNameStr, className in self.__classes.items():
            self.__reloadInstance(classNameStr, className)

    def __reloadInstance(self, prmClassNameStr, prmClassName):
        import json

        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        self.assertNotEqual(storage.all(), {})
