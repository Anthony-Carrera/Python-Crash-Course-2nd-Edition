"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default
with a message that reads I love Python. Make a large shirt and a medium shirt with the
default message, and a shirt of any size with a different message.
"""
#This created with the prefine variables
def make_shirt(size="Large",text="I Love Python"):
    print(f"\nThe '{size}' of the shirt.")
    print(f"The text of shirt '{text.title()}'")
#This just changes the variable with different input
make_shirt()
make_shirt(size="Medium")
make_shirt("Medium","I love to code")