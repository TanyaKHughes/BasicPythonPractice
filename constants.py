# constants.py - exploring with class attributes & methods and static methods


class Settings():
    height = 10  # Apparently these have to be initialized here. 
    width = 20

    def __init__(self):
        pass

    @classmethod
    def inc(cls):
        cls.height += 1
        cls.width +=1

    def inc2(self):
        #self.__class__.height += 1  This works too.
        #self.__class__.width += 1
        Settings.height += 2
        Settings.width += 2

    @staticmethod
    def add(num1, num2):
        try:
            num1, num2 = float(num1), float(num2)
        except ValueError:
            print(f"I can't add these numbers.")
            num1 = num2 = 0
        return num1 + num2


print(f"height = {Settings.height}, width = {Settings.width}")
Settings.inc()
print(f"height = {Settings.height}, width = {Settings.width}")

mine = Settings()
mine.inc2()
print(f"height = {mine.height}, width = {mine.width}")

print(f"Sum = {Settings.add(2,3)}")
print(f"Sum = {Settings.add(2,'arf')}")
