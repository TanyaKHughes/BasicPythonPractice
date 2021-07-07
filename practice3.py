# practice3.py - read and write lines from a file.

my_name = "Tanya"
his_name = 'Blake'

print(f"{my_name} and {his_name}")
print(my_name + " and " + his_name)

print(8)
print("8")
print(5+3)
print(12-4)
print(4*2)
print(16/2)

num = 21

print(f"my number = {num}\n")

filename = "poem.txt"
try:
    with open(filename) as f:
        poem_lines = f.readlines()
        print(poem_lines)
        f.seek(0)
        for line in f:
            print(line.rstrip())
except FileNotFoundError:
    print(f"Could not find file {filename}.")

filename2 = "poem2.txt"
with open(filename2,"a") as f:
    for line in poem_lines:
        f.write(line)


