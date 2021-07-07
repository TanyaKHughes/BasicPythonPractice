# calculator.py - (trying out reading from a file and exceptions)

class Calculator:
    """A simple calculator."""
    
    def __init__(self):
        self.pi = self.get_pi()

    def run(self):
        """The call to start the calculator running."""
        if not self.pi:
            return
        print("Give me two numbers and I'll add them.")
        print("Enter q to quit. Enter pi for pi.")
        while True:
            input1 = input("First number: ")
            if input1 == 'q':
                break
            if input1 == 'pi':
                input1 = self.pi
            input2 = input("Second number: ")
            if input2 == 'q':
                break
            if input2 == 'pi':
                input2 = self.pi
            try:
                num1 = float(input1)
                num2 = float(input2)
            except ValueError:
                print(f"Either {input1} or {input2} is not a number!")
                continue
            print(f"{num1} + {num2} = {num1+num2}")

    def get_pi(self):
        """Opens a file and reads the value of pi from it."""
        try:
            with open('pi.txt') as f:
                contents = f.read().strip()
        except FileNotFoundError:
            print("Couldn't find pi file.")
            return 0
        try:
            pi = float(contents)
        except ValueError:
            print("Something is wrong with the pi file.")
            return 0
        return pi                


myCalc = Calculator()
myCalc.run()
            
