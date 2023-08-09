name = ['Tony', 'Bryan', 'Chema', 'Danny']

message = f'Hello, my name is {name[0].title()}'
message1 = f'Hello, my name is {name[1].title()} I love Food'
message2 = f'Hello, my name is {name[2].title()}, I love Minecraft'
message3 = f'Hello, my name is: {name[3].title()}, how are doing?'

print(message)
print(message1)
print(message2)
print(message3)
print('\n\t')


motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(1)
print(f"The last motorcycle I owned was a {last_owned.title()}.")
