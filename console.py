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
import json
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
    __commands = ['all', 'count', 'create', 'destroy', 'show']

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
            storage.save()
            self.__printCommandResult(instance.id)
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

            self.__printCommandResult(dict[key])
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

            self.__printCommandResult(list)
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

            self.__printCommandResult(count)
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_quit(self, arg):
        raise SystemExit

    def do_EOF(self, arg):
        raise SystemExit

    def __printCommandResult(self, prmResult: str):
        print(f'{Fore.CYAN}', end='')
        print(prmResult, end='')
        print(f'{Style.RESET_ALL}')

    def __printHelp(self, prmMessage: str):
        print(f"{Fore.GREEN}", end='')
        print(prmMessage, end='')
        print(f"{Style.RESET_ALL}\n")


    def help_quit(self):
        self.__printHelp("Quit command to exit the program")

    def help_EOF(self):
        self.__printHelp("EOF command to exit the program")

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
            if self.__checkValidArguments(line):
                clName, cmd, args = self.__getArgumentsFromLine(line)
                if self.__checkValidCommand(cmd):
                    args = self.__formatArguments(args)
                    formattedCommand = self.__formatCommand(clName, cmd, args)
                    eval(formattedCommand)
                    return
                elif (cmd == 'update'):
                    parameters = self.__getParametersFromArguments(args)
                    id = self.__formatArguments(parameters[0])
                    if self.__isValidJson(parameters[1]):
                        for attribute, value in json.loads(parameters[1]).items():
                            args = "{} {} {}".format(id, attribute, value)
                            formattedCommand = self.__formatCommand(clName, cmd, args)
                            eval(formattedCommand)
                            return
                    else:
                        args = self.__formatArguments(args)
                        formattedCommand = self.__formatCommand(clName, cmd, args)
                        eval(formattedCommand)
                        return
        except:
            return super().default(line)

    def __getArgumentsFromLine(self, prmLine):
        regex = "^(.*)\.(.*)\((.*)\)$"
        regex_prog = re.compile(regex)
        results = regex_prog.findall(prmLine)
        arguments = results[0]

        return arguments

    def __isValidJson(self, prmString: str) -> bool:
        try:
            json_object = json.loads(prmString)
        except ValueError as e:
            return False
        return True

    def __getParametersFromArguments(self, prmArguments):
        regex = "^(\"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\")\, ?(.*)$"
        regex_prog = re.compile(regex)
        results = regex_prog.findall(prmArguments)
        parameters = results[0]

        return parameters

    def __checkValidArguments(self, prmLine: str) -> bool:
        arguments = self.__getArgumentsFromLine(prmLine)

        return (arguments and arguments[0] in self.__classes and
                len(arguments) == 3)

    def __checkValidCommand(self, prmCommand: str) -> bool:
        return prmCommand in self.__commands

    def __formatArguments(self, prmArguments) -> str:
        prmArguments = prmArguments.replace(", ", " ")
        prmArguments = prmArguments.replace(",", " ")
        prmArguments = prmArguments.replace('"', "")

        return prmArguments

    def __formatCommand(self, prmClassName, prmCommand, prmArguments):
        if len(prmArguments) > 0:
            arguments = "{} {}".format(prmClassName, prmArguments)
        else:
            arguments = "{}".format(prmClassName)

        return "self.do_{}(\"{}\")".format(prmCommand, arguments)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
