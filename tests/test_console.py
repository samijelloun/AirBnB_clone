#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import CustomCommand  # Changed import to use CustomCommand instead of HBNBCommand


class TestCustomCommand(unittest.TestCase):  # Changed test class name to TestCustomCommand
    """this will test the console"""

    def test_help(self):
        """test if help works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            CustomCommand().onecmd("help")  # Changed instantiation to use CustomCommand instead of HBNBCommand
        output = "EOF  all  count  create  destroy  help  quit  show  update"

    def test_create(self):
        """test if create works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            CustomCommand().onecmd("create")  # Changed instantiation to use CustomCommand instead of HBNBCommand
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_quit(self):
        """test if quit works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            CustomCommand().onecmd("quit")  # Changed instantiation to use CustomCommand instead of HBNBCommand
            self.assertTrue(f.getvalue() == "")


if __name__ == '__main__':
    unittest.main()

