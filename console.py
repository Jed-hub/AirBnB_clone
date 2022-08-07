#!/usr/bin/python3
import cmd

"""
    This module desing the console specs
"""

class HBNBCommand(cmd.Cmd):
    """
        This class provides the full functionnality of the console
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        'Quit command to exit the program'
        self.close()
        bye()
        return True

    def do_EOF(self, arg):
        """CTRL-D command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
