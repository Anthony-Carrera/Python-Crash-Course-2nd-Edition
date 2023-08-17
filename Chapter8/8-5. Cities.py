"""
8-5. Cities: Write a function called describe_city() that accepts the name of a city and
its country. The function should print a simple sentence, such as Reykjavik is in
Iceland. Give the parameter for the country a default value. Call your function for three
different cities, at least one of which is not in the default country.
"""
#This uses on the paraments to be set by Default to be USA
def describe_city(city,country ="USA"):
    print(f"{city} is in the {country}")
#This prints out the function and at the end it changes the country
describe_city("Phoenix")
describe_city("Tuscon")
describe_city("Mexico City","Mexico")