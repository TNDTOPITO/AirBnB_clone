#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = "(hbnb) "

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()