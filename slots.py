# slots.py - trying out __slots__  

# So lots of queerness here.  First, with the 
# "__slots__" line in there, you cannot add more instance attributes - either 
# values or methods - that are not defined in the original class definition, 
# even though the methods aren't listed in the "__slots__" line (only the 
# values are).  However, you can still add class attributes (methods or 
# values).  Without the  "__slots__" line, you can add ad hoc values or 
# methods as instance attributes.

class Poof:
#    __slots__ = ('a', 'b', 'c')
    d = 6

    def __init__(self, *nums):
        self.a, self.b, self.c = nums[0], nums[1], nums[2]

    def sum(self):
        return self.a + self.b + self.c + Poof.d

nums = [i for i in range(1,4)]
mine = Poof(*nums)
print(f"sum = {mine.sum()}")
    

