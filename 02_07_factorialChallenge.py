## FACTORIAL CHALLENGE

# return factorial of num if it is defined, otherwise returns NONE
def factorial(num):    
    a = []
    while (num - 1) > 0:
        a.append(num)
        num = num - 1
    print(a)
    for i in a:
        result = num
        return result * i

factorial(5)

## answer RECURSIVE

def factorial(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1
    
    return num * factorial(num - 1)
