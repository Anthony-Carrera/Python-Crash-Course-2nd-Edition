"""
7-2. Restaurant Seating: Write a program that asks the user how many people are in
their dinner group. If the answer is more than eight, print a message saying they’ll have
to wait for a table. Otherwise, report that their table is ready.
"""
#this is the input for how manny people are comming  into the dinner
people = input("How manny people your going to seat at their dinner group? ")
people = int(people)
#this checks if the party is over 8, if it is than they have to wait.
if people > 8:
    print ("Sorry, you have to wait for a table.")
else:
    print("Your table is ready shortly.")
