#update on person from the frist code in chapter 6
#this is an upate, where key is there name and item is the things they do
person = {
    'Anthony': ['Football', 'Soccer', 'Gym'],
    'Danny': ['Videos Games','Gym'],
    'Jose': ['Soccer', 'Anime', 'School'],
    'Bryan': ['Soccer', 'Math', 'School'],  
    'Manny': ['Cyber']
}
# this loop checked for everything
for name,thing in person.items():
    print(f'Hello my name is {name.title()}, here is something that I do:')
    for stuff in thing:
        print(f'{stuff.title()}')

print('\n')
people = []

# Define some people, and add them to the list.
persons = {
    'first_name': 'Anthony',
    'last_name': 'Carrera',
    'age': 21,
    'city': 'Phoenix',
    }
people.append(persons)

persons = {
    'first_name': 'Jose',
    'last_name': 'Carrera',
    'age': 5,
    'city': 'Phoenix',
    }
people.append(persons)

persons = {
    'first_name': 'Danny',
    'last_name': 'Carrera',
    'age': 8,
    'city': 'Phoenix',
    }
people.append(persons)

# Display all of the information in the dictionary.
for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    
    print(name + ", of " + city + ", is " + age + " years old.")

print('\n')

# this is a dicotry that uses the list and prints out thing we know about the pet
pets = {
    'Dog': ['Owner: Anthony', 'brown', '5ft long'],
    'Cat': ['Owner: Bryan', 'black'],
    'Frog': ['Owner: Daniel', 'green'],
    'Turtle': ['Owner: Jr','slow'],
}
# this is a for loop created to print out all the thing we know
for pet,act in pets.items():
    print(f"{pet.title()}, Things that we know about this pet")
    for acts in act:
        print(f'{acts.title()}') 
print('\n')

#list of favortive places
# debug rember the brackets & {} when making a dictornary 
favorite_places = {
    'Alex': ['Dallas', 'Phoenix', 'Miami'],
    'Danny': ['Austin', 'LA'],
    'Tony': ['Las Vegas'],
}
#this is the for loop that prints out each person favorite place
for names, places in favorite_places.items():
    print("\n" + names.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())
print('\n')

favorite_numbers = {
    'Alex': ['1', '7', '10'],
    'Danny': ['2', '8'],
    'Tony': ['4'],
}
#this is the for loop that prints out each person favorite place
for nam, num in favorite_numbers.items():
    print("\n" + nam.title() + " favorite number:")
    for nums in num:
        print("- " + nums.title())
# Differented cities
cities = {
    #City in the for loop  and the rest are a  list with country, populaation and mountains
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himilaya',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  The " + mountains + " mountains are nearby.")