"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do
each of the following at least once:
Use a conditional test in the while statement to stop the loop.
Use an active variable to control how long the loop runs.
Use a break statement to exit the loop when the user enters a
'quit' value.

"""

ages = "How old are you, this will see how much a ticket is worth"
ages += "\nEnter 'quit' when you are finished. "

num = 1
#Now I added the num variable and increase it by 1 to have the limit of 5 times that it can run it.
while num <= 5:

    age = input(ages)
    if age == 'quit':
        break
    #this checked the interger
    age = int(age)
    if age <= 3:
        print("The ticket is free.")
    elif age >= 3 and age <= 12:
        print("The ticket is $10.")
    elif age >= 12:
        print("The ticket is $15.")
    #at the end of the loop it will added the value up
    num += 1