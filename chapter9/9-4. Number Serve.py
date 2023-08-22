"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an
attribute called number_served with a default value of 0. Create an instance called
restaurant from this class. Print the number of customers the restaurant has served, and
then change this value and print it again.
Add a method called set_number_served() that lets you set the number of customers
that have been served. Call this method with a new number and print the value again.
Add a method called increment_number_served() that lets you increment the
number of customers who have been served. Call this method with any number you like
that could represent how many customers were served in, say, a day of business
"""

class Restaurant:
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
        self.serve = 0
     
    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant}")
        print(f"\nThe cuisine that we serve is {self.cuisine}")
    
    def open_restaurant(self):
        print(f"\nThe {self.restaurant} is open")
    #The two new function added the number of people who was served
    def set_number_served(self,people):
        self.serve = people
        print(f"The amount of people that been serve: {self.serve}")
    def increment_number_served(self,people):
        self.serve += people
        print(f"The amount of people that been serve: {self.serve}")


#These are the are just the new function that was added on the class.
sonic = Restaurant("Sonic", "Hamburger")
#This set the number of people was serve and increase with the increment number.
sonic.describe_restaurant()
sonic.set_number_served(10)
sonic.increment_number_served(20)
