"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a
sandwich. The function should have one parameter that collects as many items as the
function call provides, and it should print a summary of the sandwich thats being
ordered. Call the function three times, using a different number of arguments each time.
"""
#This is the function
def sandwich(*topping):
    for toppings in topping:
        print(f"The Sandwich will include the following: "+toppings)
    print("Sandwhich is Ready")
#This function will print out the topping in different lines
sandwich("Ham")
sandwich("Chicken", "Beef")
sandwich("Meat", "Steak", "Veggies")

