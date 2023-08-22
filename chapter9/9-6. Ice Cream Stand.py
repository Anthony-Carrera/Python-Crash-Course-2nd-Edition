"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class
called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1
(page 162) or Exercise 9-4 (page 167). Either version of the class will work; just pick the
one you like better. Add an attribute called flavors that stores a list of ice cream flavors.
Write a method that displays these flavors. Create an instance of IceCreamStand, and call
this method
"""
#This is a class that as used before for 9.1 exercise
class Restaurant:
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
     
    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant}")
        print(f"\nThe cuisine that we serve is {self.cuisine}")
    
    def open_restaurant(self):
        print(f"\nThe {self.restaurant} is open")

#This is the child class, It used the super funcation to get the variable from __init__
class IceCreamStand(Restaurant):
    #As well, added the flavor variable for thie code
    def __init__(self,restaurant_name,cuisine_type='ice_cream'):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []
        #created a new fuction for the falvor and print it out
    def ice_cream(self):
        for falvor in self.flavors:
            print(f"The Flavors are: {falvor.title()}")

# 
ice = IceCreamStand('Ice Cream Stand')
ice.flavors = ["Chocolate", "Vanilla", "Strawberry"]

ice.describe_restaurant()  # Calling the method from the parent class
ice.ice_cream()    # Calling the method from the child class
