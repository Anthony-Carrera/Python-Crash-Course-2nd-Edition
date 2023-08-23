"""
9-8. Privileges: Write a separate Privileges class. The class should have one attribute,
privileges, that stores a list of strings as described in Exercise 9-7. Move the
show_privileges() method to this class. Make a Privileges instance as an attribute in
the Admin class. Create a new instance of Admin and use your method to show its
privileges.
"""
#This is user class from the exercise 9.7
class User:
    def __init__(self,first_name,last_name,username,email):
        self.frist = first_name
        self.last = last_name
        self.username = username
        self.email = email
    def describe_user(self):
        print(f"\nThe user frist name is {self.frist}")
        print(f"The user last name is {self.last}")
        print(f"Username: {self.username}")
        print(f"Email : {self.email}")
        
    def greet_user(self):
        print(f"Hello {self.username}welcome in the data base")

class Admin(User):
    def __init__(self,first_name,last_name,username,email):
        super().__init__(first_name,last_name,username,email)
        
        self.privileges = Privileges()
#This make a class about privileges
class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")
 #This user admin class
user1 = Admin("Anthony", "Carrera","acarrera","acarrera@test.com")
user1.describe_user()
user1.privileges.show_privileges()
print("\n Adding privileges")
#This show the privileges and add it on the next line of code.
user1_show_privileges = ['can add post','can ban user','an delete post']

user1.privileges.privileges = user1_show_privileges
user1.privileges.show_privileges()