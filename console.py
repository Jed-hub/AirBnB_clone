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
        if arg != "BaseModel" and arg != "":
            print("** class doesn't exist **")
        elif arg == "":
            print("** class name missing **")
        else:
            model = BaseModel()
            model.save()
            print(model.id)

    def do_show(self, arg):
        """Pring the string representation of an instance"""
        n_args = len(arg.split())
        if n_args == 1:
            if arg == "BaseModel":
                print("** instance id missing **")
            else:
                print("** class doesn't exit **")

        elif n_args == 2:
            model, obj_id = [value for value in arg.split()]
            if model == "BaseModel":
                    obj = [v for v in storage.all().values() if v.id == obj_id]
                    if obj:
                        print("{}".format(obj[0]))
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")
        
    def do_all(self, arg):
        """Pring all string representation of all instances"""
        objs = storage.all()
        if arg == "" or arg == "BaseModel":
            model_list = []
            for obj in objs.values():
                model_list.append(obj.__str__())
            print(model_list)
        else:
            print("** class doesn't exist")


    def do_quit(self, arg):
        'Quit command to exit the program'
        quit()
        return True

    def do_EOF(self, arg):
        """CTRL-D command to quit the shell"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
