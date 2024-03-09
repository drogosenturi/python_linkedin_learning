import math
##  SLICING
# take a slice out of a string
name = 'my name is nik'
name[0] #prints character at 0

name[1]
name[0:7] # up to 7 but not including
name[:7] # don't need to put a 0
name[11:] # prints from 11 to the end

## similarities between strings and lists
mylist = [1,2,3,4,5]
mylist[2:4]
len(name)
len(mylist)

#   FORMATTING
# string concatenation
'my number is: '+str(5)
# an 'f string' (f stands for format)
f'my number is: {5}' # variables go in braces

f'my number is: {5} and twice that is {2*5}' # evaluating inside braces

f'Pi is: {math.pi:.2f}'

'Pi is: {}'.format(math.pi)

#   MULTI LINE STRINGS
mystring = '''
i can do a 
long block of text
as long as i want
does not stop until it sees \'\'\'
'''
mystring
print(mystring)


