"""
8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a profile of
yourself by calling build_profile(), using your first and last names and three other keyvalue pairs that describe you.
"""
def build_profile(frist,last,**options):
    user = []
    user = {
        'Frist Name': frist.title(),
        'Last Last': last.title()
    }
    for option,value in options.items():
        user[option] = value

    return user

username = build_profile('Anthony','Carrera',age =30, height= 70)
print(username)

username = build_profile('Jose','Mejia',age =10, height= 48, school = 'Middle school')
print(username)