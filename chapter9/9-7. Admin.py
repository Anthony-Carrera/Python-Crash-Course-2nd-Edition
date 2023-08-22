"""
9-7. Admin: An administrator is a special kind of user. Write a class called Admin that
inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page
167). Add an attribute, privileges, that stores a list of strings like "can add post", "can
delete post", "can ban user", and so on. Write a method called show_privileges()
that lists the administrator is set of privileges. Create an instance of Admin, and call your
method.
"""

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
#This creates the class of admin and is the child class from admin
class Admin(User):
    def __init__(self,first_name,last_name,username,email):
        super().__init__(first_name,last_name,username,email)
        self.privileges = []
        #This creates the show privlleges and prints out
    def show_privileges(self):
        print("This user is an admin and privileges it has are:")
        for privilegs in self.privileges:
            print(f"- {privilegs.title()}")
#This is the command to fill in the commands and the privileges with a list to see what and admin can do
user1 = Admin("Anthony", "Carrera","acarrera", "acarrera@test.com")
user1.privileges = ['can add post','can ban user','an delete post']

user1.describe_user()
user1.show_privileges()