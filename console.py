#!/usr/bin/python3
"""
This module contains the HBNBCommand class, which serves as the command
interpreter for the AirBnB console.
"""

import cmd
from models.base_model import BaseModel
from models import storage

current_classes = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class is a command interpreter for the AirBnB console.

    Attributes:
        prompt (str): The command prompt displayed to the user.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit the command interpreter and exit the program.

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Quit the command interpreter and exit the program.

        Usage: EOF
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print its id.

        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Print the string representation of an instance.

        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        print(req_instance)

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.

        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if class_name not in storage.classes():
                    print("** class doesn't exist **")
                elif len(args) < 2:
                    print("** instance id missing **")
                else:
                    obj_key = "{}.{}".format(class_name, args[1])
                    all_objs = storage.all()
                    if obj_key not in all_objs:
                        print("** no instance found **")
                    else:
                        del all_objs[obj_key]
                        storage.save()
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Print all string representations of instances.

        Usage: all [<class_name>]
        """
        args = arg.split()
        all_objs = storage.all()

        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in all_objs.items()])
            return
        if args[0] not in current_classes.keys():
            print("** class doesn't exist **")
            return
        else:
            print(["{}".format(str(v))
                  for _, v in all_objs.items() if type(v).__name__ == args[0]])
            return

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.

        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if class_name not in storage.classes():
                    print("** class doesn't exist **")
                elif len(args) < 2:
                    print("** instance id missing **")
                else:
                    obj_key = "{}.{}".format(class_name, args[1])
                    all_objs = storage.all()
                    if obj_key not in all_objs:
                        print("** no instance found **")
                    elif len(args) < 3:
                        print("** attribute name missing **")
                    elif len(args) < 4:
                        print("** value missing **")
                    else:
                        instance = all_objs[obj_key]
                        attribute_name = args[2]
                        attribute_value = args[3].strip('"')
                        if hasattr(instance, attribute_name):
                            attr_type = type(getattr(instance, attribute_name))
                            setattr(instance, attribute_name, attr_type(attribute_value))
                            storage.save()
                        else:
                            print("** attribute doesn't exist **")
            except NameError:
                print("** class doesn't exist **")

    def validate_classname(args, check_id=False):
        """Runs checks on args to validate classname entry.
        """
        if len(args) < 1:
            print("** class name missing **")
            return False
        if args[0] not in current_classes.keys():
            print("** class doesn't exist **")
            return False
        if len(args) < 2 and check_id:
            print("** instance id missing **")
            return False
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
