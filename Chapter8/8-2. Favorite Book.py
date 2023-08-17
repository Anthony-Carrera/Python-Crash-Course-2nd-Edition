"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my favorite
books is Alice in Wonderland. Call the function, making sure to include a book title
as an argument in the function call.
"""
#This is a funcation that ask for a parameter. In this case it will be Alice in Wonderland and will input it where it said book.title
def favorite_book(book):
    print(f"One of my favorite book is {book.title()}")

favorite_book("Alice in Wonderland")