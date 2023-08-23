from random import randint

"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of
6. Write a method called roll_die() that prints a random number between 1 and the
number of sides the die has. Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

#This is the classed that I created for the exercise
class Dice:
    def __int__(self,sides):
        self.sides = sides
    #I used this funcation to get a number from user input and than run a while loop 10 times to print out each results.
    def dice_number():
        sides = int(input("How much side you want the dice? "))
        numb = 1
        while numb <= 10:
            express = randint(1,sides)
            print(f"\nRoll: {numb};The dice you roll is {express}")
        
            numb += 1
#ran this funcation and it will asked the user input and print out 10 times

Dice.dice_number()