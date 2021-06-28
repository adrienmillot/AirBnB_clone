#!/usr/bin/python3


from os import system
from models.engine.file_storage import FileStorage
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from colorama import Fore, Style
from models import storage
from unittest_prettify.colorize import (
    BLUE,
    MAGENTA,
    colorize,
    GREEN,
    RED
)
import os

@colorize(color=MAGENTA)
class ConsolePromptingTest(unittest.TestCase):

    def testPrompt(self):
        """
            Prompt command
        """
        self.assertEqual(HBNBCommand().prompt, f"{Fore.BLUE}(hbnb){Style.RESET_ALL} ")

    def testEmptyLine(self):
        """
            Empty line
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("")
            self.assertEqual(output.getvalue().strip(), "")

@colorize(color=GREEN)
class ConsoleHelpTest(unittest.TestCase):
    def testHelpCreate(self):
        """
            create() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help create")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Creates a new instance of BaseModel, \
saves it (to the JSON file) and prints the id.\n\n")

    def testHelpAll(self):
        """
            all() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help all")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Prints all string representation of \
all instances based or not on the class name.\n\n")

    def testHelpDestroy(self):
        """
            destroy() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help destroy")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Deletes an instance based on the \
class name and id (save the change into the JSON file).\n\n")

    def testHelpUpdate(self):
        """
            update() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help update")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Updates an instance based on the \
class name and id by adding or updating attribute (save the \
change into the JSON file).\n\n")

    def testHelpShow(self):
        """
            show() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help show")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Prints the string representation of \
an instance based on the class name and id.\n\n")

    def testHelpQuit(self):
        """
            show() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help quit")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Quit command to exit the program\n\n")

    def testHelpCount(self):
        """
            count() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help count")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Update your command interpreter \
(console.py) to retrieve the number of instances of a class.\
\n\n")

@colorize(color=BLUE)
class ConsoleExitTest(unittest.TestCase):

    def testDoQuit(self):
        """
            Quit
        """
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

    def testDoEOF(self):
        """
            EOF
        """
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("EOF")

@colorize(color=BLUE)
class ConsoleAllTest(unittest.TestCase):

    classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    @colorize(color=RED)
    def testAllInvalidClass(self):
        """
            all invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("toto.all()")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    @colorize(color=RED)
    def testAllMissingClass(self):
        """
            all() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(".all()")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    def testAllInstanceSpaceNotation(self):
        """
            all instance command
        """
        self.__allInstanceSpaceNotation("Amenity", "User")
        self.__allInstanceSpaceNotation("BaseModel", "User")
        self.__allInstanceSpaceNotation("City", "User")
        self.__allInstanceSpaceNotation("Place", "User")
        self.__allInstanceSpaceNotation("Review", "User")
        self.__allInstanceSpaceNotation("State", "User")
        self.__allInstanceSpaceNotation("User", "BaseModel")

    def testAllInstanceDotNotation(self):
        """
            all() instance command
        """
        self.__allInstanceDotNotation("Amenity", "User")
        self.__allInstanceDotNotation("BaseModel", "User")
        self.__allInstanceDotNotation("City", "User")
        self.__allInstanceDotNotation("Place", "User")
        self.__allInstanceDotNotation("Review", "User")
        self.__allInstanceDotNotation("State", "User")
        self.__allInstanceDotNotation("User", "BaseModel")

    def __allInstanceSpaceNotation(self, prmClassName, prmOtherClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create {}".format(prmClassName)))
        with patch("sys.stdout", new=StringIO()) as output:
            command = "all {}".format(prmClassName)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertIn(prmClassName, output.getvalue().strip())
            self.assertNotIn(prmOtherClassName, output.getvalue().strip())

    def __allInstanceDotNotation(self, prmClassName, prmOtherClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create {}".format(prmClassName)))
        with patch("sys.stdout", new=StringIO()) as output:
            command = "{}.all()".format(prmClassName)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertIn(prmClassName, output.getvalue().strip())
            self.assertNotIn(prmOtherClassName, output.getvalue().strip())

@colorize(color=BLUE)
class ConsoleCountTest(unittest.TestCase):

    classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    @colorize(color=RED)
    def testCountMissingClass(self):
        """
            count() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("count")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    @colorize(color=RED)
    def testCountInvalidClass(self):
        """
            count() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("count toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def testCountAmenity(self):
        """
            count() Amenity
        """
        self.__testCountObject("Amenity")

    def testCountBaseModel(self):
        """
            count() BaseModel
        """
        self.__testCountObject("BaseModel")

    def testCountCity(self):
        """
            count() City
        """
        self.__testCountObject("City")

    def testCountPlace(self):
        """
            count() Place
        """
        self.__testCountObject("Place")

    def testCountReview(self):
        """
            count() Review
        """
        self.__testCountObject("Review")

    def testCountState(self):
        """
            count() State
        """
        self.__testCountObject("State")

    def testCountUser(self):
        """
            count() User
        """
        self.__testCountObject("User")

    def __testCountObject(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create {}".format(prmClassName)))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("{}.count()".format(prmClassName)))
            self.assertEqual(output.getvalue().strip(), "1")

@colorize(color=BLUE)
class ConsoleCreateTest(unittest.TestCase):

    classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    @colorize(color=RED)
    def testCreateMissingClass(self):
        """
            create() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    @colorize(color=RED)
    def testInvalidClass(self):
        """
            create() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def testCreateAmenity(self):
        """
            create() Amenity
        """
        self.__testCreateObject("Amenity")

    def testCreateBaseModel(self):
        """
            create() BaseModel
        """
        self.__testCreateObject("BaseModel")

    def testCreateCity(self):
        """
            create() City
        """
        self.__testCreateObject("City")

    def testCreatePlace(self):
        """
            create() Place
        """
        self.__testCreateObject("Place")

    def testCreateReview(self):
        """
            create() Review
        """
        self.__testCreateObject("Review")

    def testCreateState(self):
        """
            create() State
        """
        self.__testCreateObject("State")

    def testCreateUser(self):
        """
            create() User
        """
        self.__testCreateObject("User")

    def __testCreateObject(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create {}".format(prmClassName)))
            testKey = "{}.{}".format(prmClassName, output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

@colorize(color=BLUE)
class ConsoleDestroyTest(unittest.TestCase):

    classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    @colorize(color=RED)
    def testDestroyMissingClass(self):
        """
            destroy() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(output.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(".destroy()")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    @colorize(color=RED)
    def testDestroyInvalidClass(self):
        """
            destroy() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("toto.destroy()")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def testDestroyMissingIdSpaceNotation(self):
        """
            destroy missing id command
        """
        self.__missingIdSpaceNotation("Amenity")
        self.__missingIdSpaceNotation("BaseModel")
        self.__missingIdSpaceNotation("City")
        self.__missingIdSpaceNotation("Place")
        self.__missingIdSpaceNotation("Review")
        self.__missingIdSpaceNotation("State")
        self.__missingIdSpaceNotation("User")

    def testDestroyMissingIdDotNotation(self):
        """
            destroy() missing id command
        """
        self.__missingIdDotNotation("Amenity")
        self.__missingIdDotNotation("BaseModel")
        self.__missingIdDotNotation("City")
        self.__missingIdDotNotation("Place")
        self.__missingIdDotNotation("Review")
        self.__missingIdDotNotation("State")
        self.__missingIdDotNotation("User")

    def testDestroyNoInstanceFoundSpaceNotation(self):
        """
            destroy no instance command
        """
        self.__noInstanceFoundSpaceNotation("Amenity")
        self.__noInstanceFoundSpaceNotation("BaseModel")
        self.__noInstanceFoundSpaceNotation("City")
        self.__noInstanceFoundSpaceNotation("Place")
        self.__noInstanceFoundSpaceNotation("Review")
        self.__noInstanceFoundSpaceNotation("State")
        self.__noInstanceFoundSpaceNotation("User")

    def testDestroyNoInstanceFoundDotNotation(self):
        """
            destroy() no instance command
        """
        self.__noInstanceFoundDotNotation("Amenity")
        self.__noInstanceFoundDotNotation("BaseModel")
        self.__noInstanceFoundDotNotation("City")
        self.__noInstanceFoundDotNotation("Place")
        self.__noInstanceFoundDotNotation("Review")
        self.__noInstanceFoundDotNotation("State")
        self.__noInstanceFoundDotNotation("User")

    def testDestroyInstanceSpaceNotation(self):
        """
            destroy instance command
        """
        self.__destroyInstanceSpaceNotation("Amenity")
        self.__destroyInstanceSpaceNotation("BaseModel")
        self.__destroyInstanceSpaceNotation("City")
        self.__destroyInstanceSpaceNotation("Place")
        self.__destroyInstanceSpaceNotation("Review")
        self.__destroyInstanceSpaceNotation("State")
        self.__destroyInstanceSpaceNotation("User")

    def testDestroyInstanceDotNotation(self):
        """
            destroy() instance command
        """
        self.__destroyInstanceDotNotation("Amenity")
        self.__destroyInstanceDotNotation("BaseModel")
        self.__destroyInstanceDotNotation("City")
        self.__destroyInstanceDotNotation("Place")
        self.__destroyInstanceDotNotation("Review")
        self.__destroyInstanceDotNotation("State")
        self.__destroyInstanceDotNotation("User")

    def __missingIdSpaceNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy {}".format(prmClassName)))
            self.assertEqual("** instance id missing **", output.getvalue().strip())

    def __missingIdDotNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("{}.destroy()".format(prmClassName)))
            self.assertEqual("** instance id missing **", output.getvalue().strip())

    def __noInstanceFoundSpaceNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy {} 1".format(prmClassName)))
            self.assertEqual("** no instance found **", output.getvalue().strip())

    def __noInstanceFoundDotNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("{}.destroy(1)".format(prmClassName)))
            self.assertEqual("** no instance found **", output.getvalue().strip())

    def __destroyInstanceSpaceNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create {}".format(prmClassName)))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = self.__getObj(prmClassName, id)
            command = "destroy {} {}".format(prmClassName, id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

    def __destroyInstanceDotNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create {}".format(prmClassName)))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = self.__getObj(prmClassName, id)
            command = "{}.destroy({})".format(prmClassName, id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

    def __getObj(self, prmClassName: str, prmUuid: str):
        return storage.all()["{}.{}".format(prmClassName, prmUuid)]

@colorize(color=BLUE)
class ConsoleShowTest(unittest.TestCase):

    classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    @colorize(color=RED)
    def testShowMissingClass(self):
        """
            show() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    @colorize(color=RED)
    def testInvalidClass(self):
        """
            show() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def testMissingIdSpaceNotation(self):
        """
            show missing id command
        """
        self.__missingIdSpaceNotation("Amenity")
        self.__missingIdSpaceNotation("BaseModel")
        self.__missingIdSpaceNotation("City")
        self.__missingIdSpaceNotation("Place")
        self.__missingIdSpaceNotation("Review")
        self.__missingIdSpaceNotation("State")
        self.__missingIdSpaceNotation("User")

    def testMissingIdDotNotation(self):
        """
            show() missing id command
        """
        self.__missingIdDotNotation("Amenity")
        self.__missingIdDotNotation("BaseModel")
        self.__missingIdDotNotation("City")
        self.__missingIdDotNotation("Place")
        self.__missingIdDotNotation("Review")
        self.__missingIdDotNotation("State")
        self.__missingIdDotNotation("User")

    def testNoInstanceFoundSpaceNotation(self):
        """
            show no instance command
        """
        self.__noInstanceFoundSpaceNotation("Amenity")
        self.__noInstanceFoundSpaceNotation("BaseModel")
        self.__noInstanceFoundSpaceNotation("City")
        self.__noInstanceFoundSpaceNotation("Place")
        self.__noInstanceFoundSpaceNotation("Review")
        self.__noInstanceFoundSpaceNotation("State")
        self.__noInstanceFoundSpaceNotation("User")

    def testNoInstanceFoundDotNotation(self):
        """
            show() no instance command
        """
        self.__noInstanceFoundDotNotation("Amenity")
        self.__noInstanceFoundDotNotation("BaseModel")
        self.__noInstanceFoundDotNotation("City")
        self.__noInstanceFoundDotNotation("Place")
        self.__noInstanceFoundDotNotation("Review")
        self.__noInstanceFoundDotNotation("State")
        self.__noInstanceFoundDotNotation("User")

    def testShowInstanceSpaceNotation(self):
        """
            show instance command
        """
        self.__showInstanceSpaceNotation("Amenity")
        self.__showInstanceSpaceNotation("BaseModel")
        self.__showInstanceSpaceNotation("City")
        self.__showInstanceSpaceNotation("Place")
        self.__showInstanceSpaceNotation("Review")
        self.__showInstanceSpaceNotation("State")
        self.__showInstanceSpaceNotation("User")

    def testShowInstanceDotNotation(self):
        """
            show() instance command
        """
        self.__showInstanceDotNotation("Amenity")
        self.__showInstanceDotNotation("BaseModel")
        self.__showInstanceDotNotation("City")
        self.__showInstanceDotNotation("Place")
        self.__showInstanceDotNotation("Review")
        self.__showInstanceDotNotation("State")
        self.__showInstanceDotNotation("User")

    def __missingIdSpaceNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show {}".format(prmClassName)))
            self.assertEqual("** instance id missing **", output.getvalue().strip())

    def __missingIdDotNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("{}.show()".format(prmClassName)))
            self.assertEqual("** instance id missing **", output.getvalue().strip())

    def __noInstanceFoundSpaceNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show {} 1".format(prmClassName)))
            self.assertEqual("** no instance found **", output.getvalue().strip())

    def __noInstanceFoundDotNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("{}.show(1)".format(prmClassName)))
            self.assertEqual("** no instance found **", output.getvalue().strip())

    def __showInstanceSpaceNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create {}".format(prmClassName)))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = self.__getObj(prmClassName, id)
            command = "show {} {}".format(prmClassName, id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

    def __showInstanceDotNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create {}".format(prmClassName)))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = self.__getObj(prmClassName, id)
            command = "{}.show({})".format(prmClassName, id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

    def __getObj(self, prmClassName: str, prmUuid: str):
        return storage.all()["{}.{}".format(prmClassName, prmUuid)]

@colorize(color=BLUE)
class ConsoleUpdateTest(unittest.TestCase):

    classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    @colorize(color=RED)
    def testMissingClass(self):
        """
            update() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    @colorize(color=RED)
    def testInvalidClass(self):
        """
            update() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
"""
@colorize(color=BLUE)
class ConsoleTest(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        import os

        try:
            os.rename("file.json", "tmp")
        except:
            pass
            FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        import os

        try:
            os.remove("file.json")
        except:
            pass
        try:
            os.rename("tmp", "file.json")
        except:
            pass

    def testDoCreate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create toto")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        self.assertEqual(len(storage.all()), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        self.assertEqual(len(storage.all()), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Amenity")
            self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertEqual(len(storage.all()), 2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        self.assertEqual(len(storage.all()), 3)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count City")
            self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        self.assertEqual(len(storage.all()), 4)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Place")
            self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        self.assertEqual(len(storage.all()), 5)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Review")
            self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        self.assertEqual(len(storage.all()), 6)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        self.assertEqual(len(storage.all()), 7)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            self.assertEqual(f.getvalue(), "1\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        self.assertEqual(len(storage.all()), 8)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            self.assertEqual(f.getvalue(), "2\n")

    def testDoShow(self):
        import json

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show toto")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 2")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        id = self.__getUuidFromString(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity {}".format(id))
        jsonData = self.__getInitStr("Amenity", f.getvalue())
        obj = self.__getCurrentObject("Amenity", id)
        dict = self.__getInitToDict(jsonData)
        created_at = eval(dict[0])
        updated_at = eval(dict[1])
        self.assertEqual(obj.created_at, created_at)
        self.assertEqual(obj.updated_at, updated_at)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        id = self.__getUuidFromString(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(id))
        jsonData = self.__getInitStr("BaseModel", f.getvalue())
        obj = self.__getCurrentObject("BaseModel", id)
        dict = self.__getInitToDict(jsonData)
        created_at = eval(dict[0])
        updated_at = eval(dict[1])
        self.assertEqual(obj.created_at, created_at)
        self.assertEqual(obj.updated_at, updated_at)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        id = self.__getUuidFromString(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City {}".format(id))
        jsonData = self.__getInitStr("City", f.getvalue())
        obj = self.__getCurrentObject("City", id)
        dict = self.__getInitToDict(jsonData)
        created_at = eval(dict[0])
        updated_at = eval(dict[1])
        self.assertEqual(obj.created_at, created_at)
        self.assertEqual(obj.updated_at, updated_at)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        id = self.__getUuidFromString(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place {}".format(id))
        jsonData = self.__getInitStr("Place", f.getvalue())
        obj = self.__getCurrentObject("Place", id)
        dict = self.__getInitToDict(jsonData)
        created_at = eval(dict[0])
        updated_at = eval(dict[1])
        self.assertEqual(obj.created_at, created_at)
        self.assertEqual(obj.updated_at, updated_at)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        id = self.__getUuidFromString(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place {}".format(id))
        jsonData = self.__getInitStr("Place", f.getvalue())
        obj = self.__getCurrentObject("Place", id)
        dict = self.__getInitToDict(jsonData)
        created_at = eval(dict[0])
        updated_at = eval(dict[1])
        self.assertEqual(obj.created_at, created_at)
        self.assertEqual(obj.updated_at, updated_at)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        id = self.__getUuidFromString(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review {}".format(id))
        jsonData = self.__getInitStr("Review", f.getvalue())
        obj = self.__getCurrentObject("Review", id)
        dict = self.__getInitToDict(jsonData)
        created_at = eval(dict[0])
        updated_at = eval(dict[1])
        self.assertEqual(obj.created_at, created_at)
        self.assertEqual(obj.updated_at, updated_at)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        id = self.__getUuidFromString(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State {}".format(id))
        jsonData = self.__getInitStr("State", f.getvalue())
        obj = self.__getCurrentObject("State", id)
        dict = self.__getInitToDict(jsonData)
        created_at = eval(dict[0])
        updated_at = eval(dict[1])
        self.assertEqual(obj.created_at, created_at)
        self.assertEqual(obj.updated_at, updated_at)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        id = self.__getUuidFromString(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User {}".format(id))
        jsonData = self.__getInitStr("User", f.getvalue())
        obj = self.__getCurrentObject("User", id)
        dict = self.__getInitToDict(jsonData)
        created_at = eval(dict[0])
        updated_at = eval(dict[1])
        self.assertEqual(obj.created_at, created_at)
        self.assertEqual(obj.updated_at, updated_at)

    def testDoAll(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all toto")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def testDoDestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy toto")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 2")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        id = self.__getUuidFromString(f.getvalue())
        HBNBCommand().onecmd("destroy Amenity {}".format(id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Amenity {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        id = self.__getUuidFromString(f.getvalue())
        HBNBCommand().onecmd("destroy BaseModel {}".format(id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        id = self.__getUuidFromString(f.getvalue())
        HBNBCommand().onecmd("destroy City {}".format(id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy City {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        id = self.__getUuidFromString(f.getvalue())
        HBNBCommand().onecmd("destroy Place {}".format(id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Place {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        id = self.__getUuidFromString(f.getvalue())
        HBNBCommand().onecmd("destroy Review {}".format(id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Review {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        id = self.__getUuidFromString(f.getvalue())
        HBNBCommand().onecmd("destroy State {}".format(id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        id = self.__getUuidFromString(f.getvalue())
        HBNBCommand().onecmd("destroy User {}".format(id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def testDoCount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count toto")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Amenity")
            self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count City")
            self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Place")
            self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Review")
            self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            self.assertEqual(f.getvalue(), "0\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            self.assertEqual(f.getvalue(), "0\n")

    def testDoUpdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update toto")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 2")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        id = self.__getUuidFromString(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User {}".format(id))
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User {} first_name".format(id))
            self.assertEqual(f.getvalue(), "** value missing **\n")
        obj = self.__getCurrentObject("User", id)
        self.assertEqual(obj.first_name, '')
        HBNBCommand().onecmd("update User {} first_name 'John'".format(id))
        obj = self.__getCurrentObject("User", id)
        self.assertEqual(obj.first_name, 'John')
        HBNBCommand().onecmd("update User {} age 89".format(id))
        self.assertEqual(obj.first_name, 'John')
        self.assertEqual(obj.age, 89)

    def __getInitStr(self, prmClassName: str, prmString: str):
        regex = "\[" + prmClassName + "\] \(([a-fA-F0-9]{8}-[a-fA-F0-9]{4}-\
[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})\) (\{.*\})"
        regex_prog = re.compile(regex)
        self.assertRegex(prmString, regex)

        return regex_prog.findall(prmString)[0][1]

    def __getInitToDict(self, prmJson: str):
        regex = "\{'created_at': (datetime\.datetime\([0-9]{4}, \
[0-9][0-9]?, [0-9][0-9]?, [0-9][0-9]?, [0-9][0-9]?, [0-9][0-9]?, \
[0-9]{6}\)), 'updated_at': (datetime\.datetime\([0-9]{4}, [0-9][0-9]?, \
[0-9][0-9]?, [0-9][0-9]?, [0-9][0-9]?, [0-9][0-9]?, [0-9]{6}\)), \
'id': '[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-\
[a-fA-F0-9]{12}'\}"
        regex_prog = re.compile(regex)
        self.assertRegex(prmJson, regex)

        return regex_prog.findall(prmJson)[0]

    def __getUuidFromString(self, prmString: str):
        regex = "([a-fA-F0-9]{8}-\
[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-\
[a-fA-F0-9]{12})"
        regex_prog = re.compile(regex)
        results = regex_prog.findall(prmString)
        return results[0]

    def __getCurrentObject(self, prmClassName: str, prmId: str):
        return storage.all()["{}.{}".format(prmClassName, prmId)]
"""
