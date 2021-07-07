# decorator.py

## First, decorating a function that doesn't have a return value
def decorate1(func):
    def inner(name, age, home):
        print("Here's my info:")
        func(name, age, home)    
    return inner

def decorate2(func):
    def inner(name, age, home):
        if name == "Tanya":
            func(name, age, home)
            print("You're the lady of the house!")
        else:
            func(name, age, home)
    return inner

@decorate1
@decorate2
def myfunc(name, age, home):
    print(f"My name is {name}. I am {age} years old. I live in {home}.")

## Decorate a function that does have a return value
def decorate3(func):
    def inner(*args):
        return "Here's my info:\n" + func(*args)
    return inner

def decorate4(func):
    def inner(name, age, home):
        if name == "Tanya":
            return func(name, age, home) + "\nYou're the lady of the house!"
        else:
            return func(name, age, home)
    return inner

@decorate3
@decorate4
def string_together(name, age, home):
    return f"My name is {name}. I am {age} years old. I live in {home}."


# simple testing 
#mine = ["Tanya", 51, "El Dorado Hills"]
#blakes = ["Blake", 53, "the house on Basil Ct"]

#print(string_together(*mine))
#print(string_together(*blakes))
#print()

#myfunc(*mine)
#myfunc(*blakes)


######################################## Testing ##############################################
import unittest
from io import StringIO
from contextlib import redirect_stdout

class TestDecorators(unittest.TestCase):
    """Tests the functions in this file."""

    def setUp(self):
        self.mine = ["Tanya", 51, "El Dorado Hills"]
        self.blakes = ["Blake", 53, "the house on Basil Ct"]

    def test_decorator1_Tanya(self):
        expected_string = "Here's my info:\nMy name is Tanya. I am 51 years old." \
                            " I live in El Dorado Hills.\nYou're the lady of the house!"
        f = StringIO()
        with redirect_stdout(f):
            myfunc(*self.mine)
            self.assertEqual(f.getvalue().strip(), expected_string)

    def test_decorator1_not_Tanya(self):
        expected_string = "Here's my info:\nMy name is Blake. I am 53 years old." \
                            " I live in the house on Basil Ct."
        f = StringIO()
        with redirect_stdout(f):
            myfunc(*self.blakes)
            self.assertEqual(f.getvalue().strip(), expected_string)

    def test_decorators3_4_Tanya(self):
        expected_string = "Here's my info:\nMy name is Tanya. I am 51 years old." \
                            " I live in El Dorado Hills.\nYou're the lady of the house!"
        self.assertEqual(string_together(*self.mine), expected_string)

    def test_decorators3_4_not_Tanya(self):
        expected_string = ("Here's my info:\nMy name is Blake. I am 53 years old." 
                            " I live in the house on Basil Ct.")
        self.assertEqual(string_together(*self.blakes), expected_string)

if __name__ == '__main__':
    unittest.main() 
