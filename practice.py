msg = "Hello World!"
print(msg)

friends = ["Lida", "Pam", "Shannon", "Jen"]
print(friends)
print(friends[-1])

for friend in friends:
    print(f"Hello there {friend}")

places = ["Spain", "Baja", "Africa", "Fiji", "Slovakia", "Canada"]
print(places)
last = places.pop()
print(places)
places.append(last)
print(places)
places.insert(3,"Washington DC")
print(places)
places.pop(3)
print(places)
places.remove("Fiji")
print(places)
del places[0]
print(places)
print(sorted(places))
places.sort()
print(places)
places.reverse()
print(places)
print(f"length = {len(places)}")
del places[1]
print(places) 
places.sort(reverse = True)
print(places)
exit()
for i in range(1,21):
    print(i)

numbers = [num for num in range(1,101)]
for i in range(0,100):
    print(numbers[i])

millions = []
for i in range(1,1000001):
    millions.append(i)
print("min = " + str(min(millions)) + ", max = " + str(max(millions)) + " , sum = " 
       + str(sum(millions)))

odds = [num for num in range(1,21,2)]
for odd in odds:
    print(odd)

cubes = [num**3 for num in range(1,11)]
for cube in cubes:
    print(cube)

harry = 43
sally = harry
harry = 44
print("harry = " + str(harry) + ", sally =" + str(sally))

print("first 3 items are ", end = " ")
for million in millions[0:3]:
    print(million, end=" ")

print("\nlast 3 items are ", end = " ")
for million in millions[-3:]:
    print(million, end=" ")

print("\nmiddle 3 items are ", end = " ")
for million in millions[500000:500003]:
    print(million, end=" ")
print("\n")

myPizzas = ["pepperoni", "cheese", "meat lover's", "hawaiian", "special"]
hisPizzas = myPizzas[:]
hisPizzas.remove("hawaiian")
for x in myPizzas:
    print(x, end = " ")
print("\n")
for x in hisPizzas:
    print(x, end = " ")
print("\n")

# tuples
foods = ("pie", "cake", "cookies", "brownies", "donuts")
for food in foods:
    print(food, end = " ")
print("\n")

me = "Tanya"
if me is not "you":
    print("Nope")

age = int(input("How old are you?\n"))

if age < 2:
    print("you're a baby!")
elif age < 4 and age >= 2:
    print("you are a toddler!")
elif age < 65 and age >= 20:
    print("you are an adult!")
elif age < 20 and age >= 4:
    print("you're a kid!")
else:
    print("you're old!")

#fruits = ["banana", "apple", "orange", "peach", "apricot"]
fruits = []
favorite_fruits = ["peach", "apricot"]
if fruits:
    for fruit in fruits:
        if fruit in favorite_fruits:
            if fruit.endswith('ch'):
                print("you really like " + fruit + "es!")
            else:
                print("you really like " + fruit + "s!")
else:
    print("There are no fruits in the list.")
