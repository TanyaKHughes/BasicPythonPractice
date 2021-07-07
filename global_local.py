# global_local.py - use global to denote a variable that is global to the 
# file; use nonlocal to denote a variable that has a slightly wider scope 
# than the enclosing scope.  You can use a nonlocal variable if you don't 
# assign to it without declaring nonlocal; however if you try to assign
# to it python will create a new local variable of the same name.

a = 2

def func():
    global a
    a = 4
    return a

class MyClass:
    def __init__(self):
        self.b = 2

class MyOtherClass(MyClass):
    def __init__(self):
        #super().__init__()
        MyClass.__init__(self)
        self.c = 3

if __name__ == '__main__':
    print(f"a = {a}")
    print(f"func = {func()}")
    print(f"a = {a}")

    x = MyClass()
    print(f"x.b = {x.b}")
    #x.c = 3
    #print(f"x.c = {x.c}")

    y = MyOtherClass()
    print(f"y.b = {y.b}")
    print(f"y.c = {y.c}")

