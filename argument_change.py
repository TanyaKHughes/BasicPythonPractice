# argument_change.py - Python passes classes by pointer, but numbers
# by value.  The values aren't changed by the calling program, but 
# a class can be changed by the calling program.

class mine():
    def __init__(self):
        self.a = 10

def addone(i):
    i += 1
    return

def addone2(obj):
    obj.a += 1
    return


n = 1
addone(n)
print(f"n = {n}")

mine1 = mine()
addone(mine1.a)
print(f"mine1.a = {mine1.a}")

addone2(mine1)
print(f"mine1.a = {mine1.a}")
