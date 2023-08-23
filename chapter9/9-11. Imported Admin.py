"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store the
classes User, Privileges, and Admin in one module. Create a separate file, make an
Admin instance, and call show_privileges() to show that everything is working
correctl
"""
# this imports the Privileges python code And prints it out the privileges
from Privileges import Admin

user1 = Admin("Anthony", "Carrera","acarrera", "acarrera@test.com")
user1_show_privileges = ['can add post','can ban user','an delete post']

user1.describe_user()

user1.privileges.privileges = user1_show_privileges
user1.privileges.show_privileges()