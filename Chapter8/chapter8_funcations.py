#chapter 8 funcations

def greet_user(username):
#Display a simple greeting.
    print(f"Hello, {username.title()}!")

greet_user('Tony') 

def describe_pet(pet_name, animal_type='dog'):
#Display information about a pet.
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry',animal_type="cat")

def get_formatted_name(first_name, last_name, middle_name=''):
#Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


def greet_users(names):

    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
        

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
# Display all completed models.
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)