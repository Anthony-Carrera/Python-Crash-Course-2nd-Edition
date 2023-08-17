"""
8-6. City Names: Write a function called city_country() that takes in the name of a city and
its country. The function should return a string formatted like this: "Santiago, Chile"
Call your function with at least three city-country pairs, and print the values that are
returned.
"""
# This is  funcation used, This returns the value 
def city_country(city,country):
    return(city.title()+ ", " + country.title())

city = city_country('Phoenix', 'USA')
print(city)

city = city_country('Jerez', 'Mexico')
print(city)

city = city_country('Dallas', 'USA')
print(city)