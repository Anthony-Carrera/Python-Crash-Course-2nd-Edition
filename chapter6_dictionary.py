#chapter6 dictionary

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.") 

print('\n')
#create a dictoanry with a person name, age and city they in

person = {'frist_name': 'Anthony','last_name': 'Carrera','age': '21', 'city': 'Phoenix'}
#created a list with my name, age and city than print it out below
print(person['frist_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
print('\n')
#list of everone favorate number
favorite_numbers = {
    'Tony' : '7',
    'Bryan' : '10',
    'Jose'  : '14',
    'Danny' : '13',
    'Levi' : '97',
}

#this is a for loop that prints out the name and there favirote number
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")

print('\n')
#List of glossary term that is learn up to chapter 6
# the first 5 are part of the frist exercise and the other 5 are added
glossary = {
    'Code' : 'It is wrting in python',
    'Loop' : 'The loop is making the code run as much as you set it',
    'If statement' : 'The if Statement is a conditional statment, if something true it runs',
    'else if' : 'If the first condition is not true, than have a backup statement',
    'List' : 'It is an organizer, it is a way to keep a bunch of items together in a specific order',
# other 5 that are added.
    'String': 'A string is a sequence of characters, like words or sentences, enclosed in single '' or double "" lines',
    'Boolean' : 'A Boolean value is either True or False, representing the truth value of a statement',
    'Dictionary' : 'Dictionaries are used to store data values in key:value pairs',
    'Else statement' : " This statement is used when it doesn't catches anything which isn't caught by the preceding conditions",
    'Variable' : 'It is symbolic name that is a reference or pointer to an object.',
}
#this is a for loop that print out the glossary and the term
for term, meaning in glossary.items():
    print(f"{term.title()}: {meaning}\n")


#Dictionary for river and contunry, with a for loop to print it out.

water = {
    'Nile River' : 'Egypt',
    'Amazon River' : 'South America',
    'Mississippi River' : 'United States of America',
    'Congo River' : 'Democratic Republic of the Congo & Republic of the Congo',
    'Yenisei River' : 'Russia',
}

for river, country in water.items():
    print(f"{river.title()} is in {country}.")
print('\n')
#Dictionary for to see if someone has poll
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("\n")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")
print('\n')

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

print('\n')

aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
