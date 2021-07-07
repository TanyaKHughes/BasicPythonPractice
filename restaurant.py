# restaurant.py
# Exercise 9-1, 9-4, 9-6

class Restaurant:
    """A simple restaurant."""

    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.open = False
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} sells {self.cuisine_type} food.")

    def is_open(self):
        if self.open:
            print(f"{self.restaurant_name} is open!")
        else:
            print(f"{self.restaurant_name} is closed!")

    def open_restaurant(self):
        self.open = True
        self.is_open()

    def close_restaurant(self):
        self.open = False
        self.is_open()

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

class IceCreamStand(Restaurant):
    """An Ice cream stand."""

    def __init__(self, name):
        super().__init__(name, "ice cream")
        self.flavors = ["vanilla", "chocolate"]

    def describe_restaurant(self):
        print(f"{self.restaurant_name} sells {self.cuisine_type}.")

    def add_flavors(self, *flavors):
        for flavor in flavors:
            self.flavors.append(flavor)

    def display_flavors(self):
        """This just prints the flavors list as a regular human-readable list without 
            any extra punctuation."""
        if len(self.flavors) == 0:
            print("There are no flavors listed for this ice cream shop.")
            return

        display_string = ""
        for flavor in self.flavors:
            display_string += flavor + ", "
        print(display_string[:-2])    # Don't print the last comma or space
        
        # or I suppose we could just do 
        #print(*self.flavors) but that wouldn't have commas between the flavors

mystore = IceCreamStand("Tanya's Place")
mystore.describe_restaurant()
mystore.display_flavors()
mystore.flavors = []
mystore.display_flavors()
mystore.add_flavors("vanilla", "chocolate", "mint", "peanut butter")
mystore.display_flavors()
