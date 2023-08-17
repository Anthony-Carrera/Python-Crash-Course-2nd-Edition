"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on a
person age. If a person is under the age of 3, the ticket is free; if they are between 3 and
12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which
you ask users their age, and then tell them the cost of their movie ticket.
"""
# this the prompt for the age
ages = "How old are you, this will see how much a ticket is worth"
ages += "\nEnter 'quit' when you are finished. "
#This is the whie loop to checked the age, Than I put the input, than the frist command to checked the quit frist. After that checked the interger
while True:
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