"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether the number
is a multiple of 10 or not.

"""
# this ask the input of the number and make sure it is an number
number = input("Enter an Number, I see if it multiple of 10: ")
number = int(number)
# the if statment make sure if a number is disivable by 10 by checking if there is reminadar is 0
if number % 10 == 0:
    print(number , "is a multiple of 10.")
else:
    print(number , "is not a multiple of 10.")
