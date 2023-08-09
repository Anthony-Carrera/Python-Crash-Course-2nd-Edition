age = 17

if age == 18:
    print("True")
else:
    print ("False")


print("break \n")

topping = ['mushrooms', 'onions', 'pineapple']

if 'onion' in topping:
    print("This is in topping")
else:
    print("This is not in the topping")
    
print("break \n")

#conditonal test 5.1
car = 'subaru'
print("If car is subaru, I predict True.")
print(car == 'subaru')
print("\nIf the car is not audi, I predict False.")
print(car == 'audi')

print("break \n")

# contitonial test with lowertest

age = '0'
min_age = '21'
print("You are over 21?")
if age >= min_age:
    print(age >= min_age) 
else:
    print(age == min_age) 

print("break \n")

#alien color
alien_colors = ['green','yellow','red']

for alien_color in alien_colors:
    if alien_color == 'green':
        print('Have earned 5 Points')

print("break \n")
#alien color with different input for different color
alien_color1 = 'green'

if alien_color1 == 'green':
    print('You input green, have earned 5 Points')
elif alien_color1 == 'yellow':
    print('You input yellow,have earned 10 Points')
elif alien_color1 == 'red':
    print('You input red, have earned 15 Points')    
else:
    print('You input a wrong color, have earned 00 points')

print("break \n")

#stages of life code

age1 = 66

if age1 <= 2:
    print('Your are baby')
elif age1 >= 2 and age1 <= 4:
    print('Your are toddler')
elif age1 >= 4 and age1 <= 13:
    print('Your are kid')
elif age1 >= 13 and age1 <= 20:
    print('Your are teenager')  
elif age1 >= 20 and age1 <= 65:
    print('Your are an adult')
else:
    print('Your an an elder')

print("break \n")

#favorivate fruit

fav_fruit = ['organe', 'peach','green apple']

if 'apple' in fav_fruit:
    print('You really like apple')
elif 'banana' in fav_fruit:
    print('You really like banana')
elif 'cherry' in fav_fruit:
    print('You really like cherry')
else:
    print('You have no favorite fruit on the list')

print("break \n")

#user admin

users = ['Aa','Ab','Ac', 'Ad', 'Ae']
admins = ['Aa']

for user in users:
    if user in admins:
        print('Hello admin, would you like a status report')
    else:
        print('Hello',user.title(), 'thank you for logging in again.')
print("break \n")
#check for user
new_users = ["john","tom","susannah", "James"]
current_users= ["John","Tom","Susannah"]
interim_list =[]

for current_user in current_users:
    interim_list.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in interim_list:
        print ("This username, " + new_user + ", is taken")
    else:
        print ("Feel free to use " + new_user)
print("break \n")

numb = ['1','2','3','4','5','6','7','8','9']

for numbs in numb:
    if numbs in '1':
        print(f'{numbs}st')
    elif numbs in '2':
        print(f'{numbs}nd')
    elif numbs in '3':
        print(f'{numbs}rd')
    else:
        print(f'{numbs}th')
