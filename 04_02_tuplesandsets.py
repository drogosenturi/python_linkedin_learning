##  SETS
myset = {'a','b','c'}
myset
# same thing diff setup
myset = set(('a','b','c'))
myset

## if you need to remove any duplicates from a list
mylist = ['a','b','b','c','c'] # has duplicates
mylist = list(set(mylist)) # convert to set and push back thru list
mylist # no longer has duplicates (the order is NOT the same)

myset[0] # cant find the postion because sets are not ordered
number = 1
1[0] # not subscriptable

myset.add('d') # use add function to add something to 'the pile'
myset
'a' in myset # true
'z' in myset # false

len(myset) # u can get the length

while len(myset):
    print(myset.pop())
myset # now empty cause of pop
myset = {'a','b','c'}
myset.discard('a') # to get rid of a set element
myset

##  TUPLES
mytuple = ('a','b','c')
mytuple
## cannot modify
mytuple[0]
mytuple[0] = 'd' # cant add to tuple!

## fixed capacity in memory

def returnsMultipleValues():
    return 1,2,3 # tuple with or without parentheses, no parentheses by standard
type(returnsMultipleValues()) # of type tuple by default!

mytuple = 1,2,3 # USE PARENTEHSES BY TRADITION
type(mytuple) # tuple by default, even without parentheses

#   "unpacking values"
a, b, c = returnsMultipleValues()
print(a)
print(b)
print(c)