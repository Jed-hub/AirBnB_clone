#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel

"""
    This module desing the console specs
"""


class HBNBCommand(cmd.Cmd):
    """
        This class provides the full functionnality of the console
        List of commands:
            -create : To create a new instance of BaseModel
            
            -show: Prints the string representation of an instance

            -destroy: Deletes an instance

            -all: Prints all string representation of all instances

            -update: Update an instance
    """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of a BaseModel"""
        if arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            model = BaseModel()
            model.save()

    def do_show(self, arg):
        if arg == "" or arg == "BaseModel":
            model_list = []
            model_list.append(storage.all())

    def do_all(self, arg):
        """Pring all string representation of all instances"""
        storage.all()


    def do_quit(self, arg):
        'Quit command to exit the program'
        quit()
        return True

    def do_EOF(self, arg):
        """CTRL-D command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
