test = ['pepperzoni', 'ham', 'cheese']
pet = ['dog', 'cat', 'bird']
for tests in test:
    print(f"I love {tests.title()} pizza! ")
    
print(f"I really love pizza!")

for pests in pet:
    print(f"A {pests.title()} would make a pet!")

print('Any of these animals would make a great pet!')

odd_numbers = []
for number in range(1, 21):
    if number % 2 != 0:
        odd_numbers.append(number)

for odd_number in odd_numbers:
    print(odd_number)