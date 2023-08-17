"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza
toppings until they enter a 'quit' value. As they enter each topping, print a message
saying you will add that topping to their pizza.
"""
#this creates the Prompt for the pizza
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "
#This checks the condition is true. If so it runs a while loop until the loop is flase and break
while True:
    topping = input(prompt)
    if topping != 'quit':
        print(" I'll add " + topping + " to your pizza.")
    else:
        print("Your pizza will be reday shorty")
        break