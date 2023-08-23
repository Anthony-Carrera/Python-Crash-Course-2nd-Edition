"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and five letters.
Randomly select four numbers or letters from the list and print a message saying that any
ticket matching these four numbers or letters wins a prize.
"""
from random import choice
#This is the list of 5 letter and 10 numbers
chacter = ['A','B','C','D','E','1','2','3','4','5','6','7','8','9']
#empty array to append the list and than it pull the different choice that it not the same
wining =[]
while len(wining) < 4:
    pulled_item = choice(chacter)
    if pulled_item not in wining:
        print(f"  We pulled a {pulled_item}!")
        wining.append(pulled_item)
