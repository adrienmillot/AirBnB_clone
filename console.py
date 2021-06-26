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
import re
from colorama import Fore, Style


class HBNBCommand(cmd.Cmd):
    """
        Console
    """
    prompt = f"{Fore.BLUE}(hbnb){Style.RESET_ALL} "
    __classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
    ]
    __commands = ['all', 'count', 'create', 'destroy', 'show', 'update']

    def do_create(self, prmArg):
        """
            Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id.
        """
        try:
            if not prmArg:
                raise ValueError("** class name missing **")

            args = prmArg.split()

            if args[0] not in self.__classes:
                raise ValueError("** class doesn't exist **")

            instance = eval(args[0])()
            print(f'{Fore.CYAN}', end='')
            print(instance.id, end='')
            print(f'{Style.RESET_ALL}')
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

            print(f'{Fore.CYAN}', end='')
            print(dict[key], end='')
            print(f'{Style.RESET_ALL}')
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_all(self, prmArg):
        """
            Prints all string representation of all instances based or not
            on the class name.
        """
        try:
            list = []

            args = prmArg.split()

            if args[0] not in self.__classes:
                raise ValueError("** class doesn't exist **")

            for key, value in storage.all().items():
                if args[0] is None or args[0] == type(value).__name__:
                    list.append(str(value))

            print(f'{Fore.CYAN}', end='')
            print(list, end='')
            print(f'{Style.RESET_ALL}')
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

            className, command, attribute, value = args

            if value[0] != '"':
                value = '"' + value
            if value[-1] != '"':
                value = value + '"'

            if attribute not in ("id", "created_at", "updated_at"):
                setattr(obj, attribute, value[1:-1])
                storage.save()
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_count(self, prmArg):
        """
            Update your command interpreter (console.py) to retrieve the number
            of instances of a class.
        """
        try:
            count = 0
            if not prmArg:
                raise ValueError("** class name missing **")

            args = prmArg.split()

            if args[0] not in self.__classes:
                raise ValueError("** class doesn't exist **")

            for key, value in storage.all().items():
                if args[0] is None or args[0] == type(value).__name__:
                    count += 1

            print(f'{Fore.CYAN}', end='')
            print(count, end='')
            print(f'{Style.RESET_ALL}')
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_quit(self, arg):
        raise SystemExit

    def do_EOF(self, arg):
        raise SystemExit

    def help_quit(self):
        print(f"{Fore.GREEN}Quit command to exit the program{Style.RESET_ALL}\n")

    def help_EOF(self):
        print(f"{Fore.GREEN}EOF command to exit the program{Style.RESET_ALL}\n")

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

    def default(self, line: str) -> bool:
        """
            Called when command prefix is not recognized in order
            to verify and catch or not the adequate function.
        """
        try:
            regex = "^(.*)\.(.*)\((.*)\)$"
            regex_prog = re.compile(regex)
            results = regex_prog.findall(line)
            args = results[0]
            if args and args[0] in self.__classes and len(args) == 3:
                className, command, arguments = args
                if command in self.__commands:
                    arguments = arguments.replace(", ", " ")
                    arguments = arguments.replace(",", " ")
                    arguments = arguments.replace('"', "")
                    if len(arguments) > 0:
                        arguments = "{} {}".format(className, arguments)
                    else:
                        arguments = "{}".format(className)
                    print("self.do_{}(\"{}\")".format(command, arguments))
                    eval("self.do_{}(\"{}\")".format(command, arguments))
                    return
        except:
            return super().default(line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
