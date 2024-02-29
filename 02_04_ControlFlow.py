## CONTROL FLOW

# if statement

a = True
if a:
    print('it is true')
    print('also print this')
else:
    print('it is false')
print('always print this')

# multiple if statements
a = True
b = True
c = True
if a:
    print('it is true')
    print('also print this')
    if b:
        print('both are true')
        if c:
            print('all 3 true')
else:
    print('it is false')
print('always print this')

# LOOPS
a = [1,2,3,4,5]
for item in a: # can use anything in place of item
    print(item)

# while loop
a = 0 
while a < 5:
    print(a)
    a = a + 1


