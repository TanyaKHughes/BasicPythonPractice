# IceCreamStand2.py - I just wanted to recreate this in a different file to see
# if it would still work

import restaurant as r

class IceCreamStand2(r.Restaurant):
    """An Ice cream stand."""

    def __init__(self, name):
        super().__init__(name, "ice cream")
        # or, rather: r.Restaurant.__init__(self, name, "ice cream")
        self.flavors = ["vanilla", "chocolate"]

    def describe_restaurant(self):
        print(f"{self.restaurant_name} sells {self.cuisine_type}.")

    def add_flavors(self, *flavors):
        for flavor in flavors:
            self.flavors.append(flavor)

    def display_flavors(self):
        print(tuple(self.flavors)) 
