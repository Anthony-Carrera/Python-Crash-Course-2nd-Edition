"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different
instances from the class, and call describe_restaurant() for each instance.
"""

#This resuse code of 9.1 Restaurant
class Restaurant:
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
     
    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant}")
        print(f"\nThe cuisine that we serve is {self.cuisine}")
    
    def open_restaurant(self):
        print(f"\nThe {self.restaurant} is open")
#These are the 3 instance that asked for in the exercise.
soinc = Restaurant("Sonic", "Hamburger")
steak_house = Restaurant("Stockyards Restaurant", "Steak")
tacos = Restaurant("Los Valle Cocina Mexicana", "Tacos")

soinc.describe_restaurant()
soinc.open_restaurant()

steak_house.describe_restaurant()
steak_house.open_restaurant()

tacos.describe_restaurant()
tacos.open_restaurant()