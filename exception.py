# exception.py - just some basic exception practice

n = int(input("Enter a number and I'll divide 100 by your number: "))

try:
    dividend = 100/n
except ZeroDivisionError:
    print("I can't divide by zero!")
else:
    print(f"I did it! The answer is {dividend:.2f}, or {dividend:.1%}")

print(f"Your number was: {n}")
