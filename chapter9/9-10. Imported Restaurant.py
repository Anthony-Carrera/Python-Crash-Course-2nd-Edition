"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance, and call one
of Restaurantis  methods to show that the import statement is working properly
"""
#This just import and it will print out the variable
from IceCreamStand import Restaurant

rest = Restaurant('Sonic', 'Hamburger')
rest.describe_restaurant()
rest.open_restaurant()