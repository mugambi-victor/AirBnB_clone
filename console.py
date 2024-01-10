#!/usr/bin/python3
"""
This module holds the implementation of the cmd module to
form the prompt
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    class definition for the entry point for the command interpreter
    """

    prompt = '(hbnb)'

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def do_EOF(self, arg):
        'Exits'
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()