#!/usr/bin/python3
"""
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import string


class HBNBCommand(cmd.Cmd):
    """
        Console
    """
    prompt = "(hbnb) "
    __classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

    def do_create(self, prmArg):
        """
            Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id.
        """
        try:

            if not prmArg:
                raise ValueError("** class name missing **")
            if prmArg not in self.__classes:
                raise ValueError("** class doesn't exist **")

            instance = eval(prmArg)()
            print(instance.id)
            storage.save()
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_show(self, prmArgs):
        """
            Prints the string representation of an instance based on the
            class name and id.
        """
        try:
            if not prmArgs:
                raise ValueError("** class name missing **")

            args = prmArgs.split()

            if args[0] not in self.__classes:
                raise ValueError("** class doesn't exist **")
            if len(args) == 1:
                raise ValueError("** instance id missing **")

            dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in dict:
                raise ValueError("** no instance found **")

            print(dict[key])
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_all(self, prmArg):
        """
            Prints all string representation of all instances based or not
            on the class name.
        """
        try:
            list = []

            if prmArg is None or prmArg not in self.__classes:
                raise ValueError("** class doesn't exist **")

            for key, value in storage.all().items():
                if prmArg is None or prmArg == type(value).__name__:
                    list.append(str(value))

            print(list)
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_destroy(self, prmArgs):
        """
            Deletes an instance based on the class name and id (save the change
            into the JSON file).
        """
        try:
            if not prmArgs:
                raise ValueError("** class name missing **")

            args = prmArgs.split()

            if args[0] not in self.__classes:
                raise ValueError("** class doesn't exist **")
            if len(args) == 1:
                raise ValueError("** instance id missing **")

            dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in dict:
                raise ValueError("** no instance found **")

            del dict[key]
            storage.save()
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_update(self, prmArgs):
        """
            Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
        """
        try:
            if not prmArgs:
                raise ValueError("** class name missing **")

            args = prmArgs.split()

            if args[0] not in self.__classes:
                raise ValueError("** class doesn't exist **")
            if len(args) == 1:
                raise ValueError("** instance id missing **")

            dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in dict:
                raise ValueError("** no instance found **")
            obj = dict[key]

            if len(args) == 2:
                raise ValueError("** attribute name missing **")
            if len(args) == 3:
                raise ValueError("** value missing **")

            if args[2] not in ("id", "created_at", "updated_at"):
                setattr(obj, args[2], args[3][1:-1])
                storage.save()
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_quit(self, arg):
        raise SystemExit

    def do_EOF(self, arg):
        raise SystemExit

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("EOF command to exit the program\n")

    def help_create(self):
        pass

    def help_show(self):
        pass

    def help_all(self):
        pass

    def help_destroy(self):
        pass

    def help_update(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
