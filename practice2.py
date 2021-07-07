# Practice2.py

# starting with dictionaries (Chapter 6)

py_dict = {
    'dictionary': "hash table, designate with {'Bob': 'artist', 'John': 'carpenter'}",
    'list': "fancy array, designate with ['Bob', 'John']",
    'tuple': "immutable list, designate with (200, 5)",
    'elif': 'else if',
    'then': "doesn't exist",
    'range': 'use in for loops',
    'True': 'bool words are lower-case, capitalized',
    'key-value pairs': 'used in dictionary',
}

print("\n")
for k, value in sorted(py_dict.items()):  # come back to sorting independent of case when you know what a 
                                          # lambda is
    print(k.title() + " - " + value)

print("\n")
river_locations = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states',
    'seine': 'france',
}

for river, location, in river_locations.items():
    print("The " + river.title() + " River is in " + location.title() + ".")

print("\nRivers included are:")
for river in river_locations:
    print("\t" + river.title())
print("\nLocations include:")
for location in river_locations.values():
    print("\t" + location.title())

people = ['Lisa', 'Stephanie', 'Blake', 'Aaron', 'Tanya', 'Sarah']
fav_lang = {
    'Lisa': 'French',
    'Aaron': 'Spanish',
    'Tanya': 'Latin',
}
print("\n")
for person in people:
    if person in fav_lang.keys():
        print("Thank you " + person.title() + " for responding.")
    else:
        print(person.title() + ", please respond to the survey.")

print("\n") # Ch. 7
sandwich_orders = [
    'pastrami',
    'tuna', 
    'veggie',
    'pastrami', 
    'turkey', 
    'roast beef', 
    'pastrami', 
    'ham', 
    'egg salad']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    wich = sandwich_orders.pop()
    print("Making a " + wich + " sandwich.")
    finished_sandwiches.append(wich)
print('\n')
for wich in finished_sandwiches:
    print("Completed " + wich + " sandwich order.")

print('\n')
responses = {}
polling_active = True
while polling_active:
    name = input("What's your name?  ")
    location = input("What's your dream vacation spot?  ")
    responses[name] = location
    repeat = input("Is anyone else there to take the poll?  ")
    if repeat == 'no':
        polling_active = False
print('\n')
print(responses)
for name, location in responses.items():
    print(name.title() + " wants to go to " + location.title() + ".")



