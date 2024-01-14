#!/usr/bin/python3
"""
This module holds the implementation of the cmd module to
form the prompt
"""

import cmd
import models
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    class definition for the entry point for the command interpreter
    """

    prompt = '(hbnb)'
    valid_classes = [
            "BaseModel", "City",
            "Amenity", "Review",
            "Place", "State", "User"
            ]

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def do_EOF(self, arg):
        'Exits'
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of a specified
        class,
        saves it (to a JSON file), and prints the id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representations of all
        instances based on the class name."""
        args = arg.split()
        if args and args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        class_name = args[0] if args else None
        if class_name:
            instances = [
                    str(value) for key, value in models.
                    storage.all().items() if key.startswith(class_name + ".")]
        else:
            instances = [
                    str(value) for key, value in
                    models.storage.all().items()
                    ]
        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating an attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        instance = models.storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_count(self, arg):
        """Counts the number of instances of a class."""
        class_name = arg.split()[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        instances = [
                value for key, value in
                models.storage.all().items()
                if key.startswith(class_name + ".")
                ]
        print(len(instances))

    def default(self, arg):
        """
        Default behavior for cmd module
        when input is invalid
        """
        argument_list = arg.split('.')

        classs_name = argument_list[0]  # incoming class name
        if len(argument_list) < 2:
            print("** Invalid class name: {}".format(classs_name))
            return False
        command = argument_list[1].split('(')
        cmd_method = command[0]  # incoming command method
        e_arg = command[1].split(')')[0]  # extra arguments
        method_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }

        if cmd_method in method_dict.keys():
            if cmd_method == "all" and e_arg == "":
                # Handle the case of "<class name>.all()"
                return self.do_all(classs_name)
            elif cmd_method != "update":
                return method_dict[
                        cmd_method]("{} {}".format(
                            classs_name, e_arg))
            else:
                if not classs_name:
                    print("** class name missing **")
                    return

                try:
                    call = method_dict[cmd_method]
                    return call("{} {}".format(classs_name, e_arg))
                except Exception:
                    pass
        else:
            print("*** Unknown syntax: {}".format(arg))
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
