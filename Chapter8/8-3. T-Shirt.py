"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a
message that should be printed on the shirt. The function should print a sentence
summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a
second time using keyword arguments.
"""
#This is a funcation that asked for the size and text of the shirt, As well keyword argument. Which is a name-value pair that you pass to a function.
def make_shirt(size,text):
    print(f"\nThe '{size}' of the shirt.")
    print(f"The text of shirt '{text.title()}'")
#This is the input and the keyword argument input
make_shirt("Large", "Cool")
make_shirt(size="Small", text="I love to Code")