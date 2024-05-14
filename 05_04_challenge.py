# write a function that returns a list of all prime numbers up to
# the given input number

def allPrimesUpTo(num):
    primelist = [2]
    for x in range(3, num):
        sqrt = x ** 0.5
        for i in primelist:
            if x % i == 0:
                break
            #x = x + 1
            if i > sqrt:
                primelist.append(x)
                break
    return primelist

allPrimesUpTo(1000)

x = 2.2
type(3/2) != int
n = 4 % 2
n != 0
print(n)

list = [1,2,3,4,5]
list[-1]