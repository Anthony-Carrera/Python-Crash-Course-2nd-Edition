"""
9-1.Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a
method called describe_restaurant() that prints these two pieces of information, and a
method called open_restaurant() that prints a message indicating that the restaurant is
open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
"""
#This is the class for this example
class Restaurant:
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
    #This desrcibe the restaraunts 
    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant}")
        print(f"\nThe cuisine that we serve is {self.cuisine}")
    #This describe if the restaurants is open.
    def open_restaurant(self):
        print(f"\nThe {self.restaurant} is open")

a = Restaurant("Sonic", "Hamburger")
#This prints out the variable a and funcations that are in side of the class.
print(a.restaurant)
print(a.cuisine)

a.describe_restaurant()
a.open_restaurant()