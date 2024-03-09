##  LIST SLICING
mylist = [1,2,3,4,5]
mylist[3:]
mylist[0:6:2] ## last is the step size
mylist[::2] ## step two from beginning to end

for i in range(100):
    print(i)
mylist = list(range(100))

mylist[::-10] # step backwards through list with negatives

##  MODIFYING LISTS
mylist = [1,2,3,4,5]
mylist.append(6) ## append to the end of the list
print(mylist)

# insert in a specific position
mylist.insert(3, 'a new value') # insert this string at position 3
print(mylist)

mylist.remove('a new value')
print(mylist)

mylist.pop() # removes last item from list and returns it to you
print(mylist)

while len(mylist):
    print(mylist.pop())
print(mylist) ## emptied out list 

a = [1,2,3,4,5]
b = a
a.append(6)
print(b) # b changes with a in this case

a = [1,2,3,4,5]
b = a.copy()
a.append(6)
print(a)
print(b) # with a.copy, b stays the same as the original a

