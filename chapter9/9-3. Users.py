"""
9-3. Users: Make a class called User. Create two attributes called first_name and
last_name, and then create several other attributes that are typically stored in a user
profile. Make a method called describe_user() that prints a summary of the user’s
information. Make another method called greet_user() that prints a personalized
greeting to the user.
Create several instances representing different users, and call both methods for each
user.
"""
#This is the class about the user 
class User:
    #This funcation that adds the attribues for the user 
    def __init__(self,first_name,last_name,username,email):
        self.frist = first_name
        self.last = last_name
        self.username = username
        self.email = email
        #This function printes out all the user info
    def describe_user(self):
        print(f"\nThe user frist name is {self.frist}")
        print(f"The user last name is {self.last}")
        print(f"Username: {self.username}")
        print(f"Email : {self.email}")
        #This function prints out the user a welcome
    def greet_user(self):
        print(f"Hello {self.username}welcome in the data base")
#This a variable of user and at the bottom it prints it out.
user1 = User("Anthony", "Carrera","acarrera", "acarrera@test.com")    
user2 = User("Anthony", "Mejia","amejia", "amejia@test.com")
user3 = User("Juan", "Acuna","jacuna","jacuna@test.com")  

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()