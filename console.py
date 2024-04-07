#!/usr/bin/python3
"""This module represents this console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import json


class_mapping = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ This method represents quit"""
        return True

    def do_EOF(self, arg):
        """ This method represents EOF"""
        print()
        return True

    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program")
        print()

    def do_quit(self, line):
        """ This method represents quit Commande"""
        return True

    def emptyline(self):
        """This module represents empty line """
        pass

    def do_create(self, arg):
        """ This method represents create"""
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """This function defines the destroy method"""
        try:
            args = []
            args = arg.split()
            lenght = len(args)

            if lenght == 0:
                print("** class name missing **")
            elif lenght == 1:
                print("** instance id missing **")
            elif args[0] not in class_mapping:
                print("** class doesn't exist **")
            else:
                key_to_delete = "{}.{}".format(args[0], args[1])
                storage_dict = models.storage.all()
                try:
                    del storage_dict[key_to_delete]
                    models.storage.save()
                except KeyError:
                    print("** no instance found **")
        except IndexError:
            pass

    def do_all(self, arg):
        """This function represents all instance"""
        listall = []
        listarg = []
        storage_dict = models.storage.all()
        if arg not in class_mapping and len(arg) != 0:
            print("** class doesn't exist **")
        for v in storage_dict.values():
            listall.append(str(v))
        if arg:
            if arg in class_mapping:
                for i in listall:
                    if arg in i:
                        listarg.append(i)
                print(listarg)
        else:
            print(listall)

    def do_count(self, arg):
        """This function represents count instance"""
        listall = []
        listarg = []
        storage_dict = models.storage.all()
        count_ = 0

        if arg not in class_mapping and len(arg) != 0:
            print("** class doesn't exist **")
        for v in storage_dict.values():
            listall.append(str(v))
            count_ += 1
        if arg:
            count_ = 0
            if arg in class_mapping:
                for i in listall:
                    if arg in i:
                        listarg.append(i)
                        count_ += 1
                print(count_)
            else:
                print(count_)

    def do_show(self, line):
        """This method represents show instance"""
        try:
            args = line.split()
            lenght = len(args)
            class_name = args[0]
            instance_id = args[1]
            key = class_name + "." + instance_id
            objects = models.storage.all()
            if class_name not in class_mapping:
                print("** class doesn't exist **")
            elif instance_id is not True:
                print("** no instance found **")
            if key in objects:
                print(objects[key])

        except IndexError:
            if lenght == 0:
                print("** class name missing **")
            if lenght == 1:
                if args[0] in class_mapping:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        except KeyError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        try:
            args = arg.split()
            if not args:
                print("** class name missing **")
                return

            class_name = args[0]
            if class_name not in class_mapping:
                print("** class doesn't exist **")
                return
            instances = models.storage.all()
            instance_id = args[1]
            key = class_name + "." + instance_id
            attr_name = args[2]
            if attr_name[0] == '"' and attr_name[-1] == '"':
                attr_name = attr_name[1:-1]

            attr_value = args[3]
            if attr_value[0] == '"' and attr_value[-1] == '"':
                attr_value = attr_value[1:-1]
            if str(attr_value) is True:
                attr_value = attr_value[1:-1]
            try:
                attr_value = int(attr_value)
            except ValueError:
                try:
                    attr_value = float(attr_value)
                except ValueError:
                    pass
            try:
                instance = instances[key]
                setattr(instance, attr_name, attr_value)
                instance.save()
            except KeyError:
                if args[0] in class_mapping:
                    print("** no instance found **")
                else:
                    print("** class doesn't exist **")
        except IndexError:
            if len(args) < 2:
                print("** instance id missing **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return

    def default(self, arg):
        """This function represents the default value."""
        try:

            listarg = arg.split('(')
            list_left = listarg[0].split('.')
            function_ = list_left[1]
            class_ = list_left[0]

            if len(listarg) == 2:
                if function_ == 'all':
                    self.do_all(class_)
                elif function_ == 'count':
                    self.do_count(class_)
                elif function_ == 'show':
                    instance_id = listarg[1].strip(')\"')
                    self.do_show(f"{class_} {instance_id}")
                elif function_ == 'destroy':
                    instance_id = listarg[1].strip(')\"')
                    self.do_destroy(f"{class_} {instance_id}")
                elif function_ == 'update':
                    update_args = listarg[1].rstrip(')').split(', ', 1)
                    instance_id = update_args[0].strip().strip('"')
                    print(update_args[1])
                    if isinstance(update_args[1], dict)  \
                       or "{" in update_args[1]:
                        update_args[1] = update_args[1].strip('{}')
                        update_new = update_args[1].split(', ')
                        update_dict = {item.split(': ')[0]: item.split(': ')[
                            1] for item in update_new}
                        for k, v in update_dict.items():
                            k = k.strip('"\'')
                            self.do_update(f"{class_} {instance_id} {k} {v}")
                    else:
                        update_new = update_args[1].split(',')
                        attr_name = update_new[0].strip().strip('"')
                        attr_value = update_new[1].strip()
                        self.do_update(
                            f"{class_} {instance_id} \
                            {attr_name} {attr_value}")

        except IndexError:
            print("** invalid command **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
