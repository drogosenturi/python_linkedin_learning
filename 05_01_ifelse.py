## if statements with Fizz and Buzz
# the if else way
for n in range(1, 101):
    if n % 15 == 0:
        print('FizzBuzz')
    else:
        if n % 3 == 0:
            print('Fizz')
        else:
            if n % 5 == 0:
                print('Buzz')
            else:
                print(n)

# the elif way
for n in range(1, 101):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
# write an if statement, any number of elif statements, and end with else

# single line if statements
n = 5
print('Fizz' if n % 3 == 0 else n)
# as a ternary operator
fizzBuzz = 'Fizz' if n % 3 == 0 else n
fizzBuzz
'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n

'FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n
# in a list
['FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n]
