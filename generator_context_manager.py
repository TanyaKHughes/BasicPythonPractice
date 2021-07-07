# generator_context_manager.py
# This contains some simple examples:  a generator, and a context manager done 3 ways.  
# All of the outputs from the 3 different context managers should be the same (except 
# for the input numbers!)..
# You can also make an iterator that is a class by implementing __iter__() and 
# __next__() methods.  So then you can iterate over an instance of the class. But the
# generator function is easier than making an iterator class.

from contextlib import contextmanager

# a generator function creates a generator iterator, which is an object that 
# you can call next() on.   ie, if a = gen(10), you can call next(a).
def gen(num):
    """A simple generator function"""
    for i in range(0,9):
        yield num + i

for num in gen(10):
    print(num)

@contextmanager
def func(num):
    """A simple function to work within a context.  It runs to the yield statement within 
        the with block; then after the with block it returns and finishes out the rest of
        the function."""
    yield num + 1
    print(f"The number was {num}.")

with func(10) as n:
    print(n)


@contextmanager
def func2(num):
    """Or you might want to use try/finally so that if something in the function fails,
        you still have the resource cleanup getting done."""
    try:
        yield num + 1
    finally:
        print(f"The number was {num}.")

with func2(20) as n:
    print(n)

class MyContextClass:
    """A simple class that works with context management. You just need to add 
        __enter__ and __exit__ methods to any class to make it happen."""
    def __init__(self,num):
        self.num = num

    def __enter__(self):
        return self.num + 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"The number was {self.num}")

with MyContextClass(30) as my_num:
    print(my_num)

# Or, you can write your own decorator that is a context manager:
from contextlib import ContextDecorator

class MyContextDecoratorClass(ContextDecorator):
    __enter__(self):
        pass
    __exit__(self):
        pass

# This would allow you to define tasks to do before and after a function.  But you can
# already do that with a basic decorator function, right? I guess this allows you to 
# use it with the "with" statement or as a decorator. Both of those constructs allow you 
# to add on extra functionality to a function/action.

# with MyContextDecoratorClass():
    # do something

# or

# @MyContextDecoratorClass
# myfunc():
#   do something
