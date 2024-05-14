# for loops!
myList = [1,2,3,4]
for item in myList:
    print(item)

# pass statements in for loop
animalLookup = {
    'a': ['aardvark', 'antelope'],
    'b': ['bear'],
    'c': ['cat'],
    'd': ['dog'],
}
for letter, animals in animalLookup.items():
    pass

# continue to skip items
for letter, animals in animalLookup.items():
    if len(animals) > 1:
        continue
    print(f'Only one animal {animals}')

# break
for letter, animals in animalLookup.items():
    if len(animals) > 1:
        print(f'Found {len(animals)} animals: {animals}')
        break # stops after the first instance

# break else/for else
# finding prime numbers between 2 and 100
for number in range(2, 100):
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            break
    else:
        print(f'{number} is prime')

## longer dumb way
for number in range(2, 100):
    found_factors = False
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            found_factors = True
            break
    if not found_factors: # use else instead, obviously.
        print(f'{number} is prime')
