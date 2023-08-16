#8/15/2023 Basic input asking the user it name
promt = "Tell me more about your self?"
promt += "\nWhat is your age? "

name = int(input(promt))

if name > 21:
    print("You are over 21")
elif name == 21:
    print("Your 21")
else:
    print("Your under 21")

print('\n')

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
