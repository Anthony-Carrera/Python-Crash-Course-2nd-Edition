"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class from
Exercise 9-3 (page 162). Write a method called increment_login_attempts() that
increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several
times. Print the value of login_attempts to make sure it was incremented properly, and
then call reset_login_attempts(). Print login_attempts again to make sure it was
reset to 0.
"""

class User:
    
    def __init__(self,first_name,last_name,username,email):
        self.frist = first_name
        self.last = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0

        
    def describe_user(self):
        print(f"\nThe user frist name is {self.frist}")
        print(f"The user last name is {self.last}")
        print(f"Username: {self.username}")
        print(f"Email : {self.email}")
        
    def greet_user(self):
        print(f"Hello {self.username}welcome in the data base")


    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0

#This a variable of user and at the bottom it prints it out.
user1 = User("Anthony", "Carrera","acarrera", "acarrera@test.com")

user1.describe_user()
user1.greet_user()
#This prints out the loggin attempt and at the end it clears it.
print("\nMaking 3 login attempts...")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"  Login attempts: {user1.login_attempts}")

print("Resetting login attempts...")
user1.reset_login_attempts()
print(f"  Login attempts: {user1.login_attempts}")