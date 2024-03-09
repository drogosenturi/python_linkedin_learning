##  DICTIONARY COMPREHENSIONS
animalList = [('a','aardvark'), ('b','bear'),('c','cat'), ('d','dog')]
# list of tuples

# make dictionary from listof tuples
animals = {item[0]: item[1] for item in animalList}
animals # now a dictionary, similar to list comprenhension

animals = {key: value for key, value in animalList}
animals # more concise way without using positions

#animals = {key: value for key, value, itemthree in animalList}
animals # this doesn't work because there are only 2 values to unpack,
# but we tell it to unpack 3

# turn dictionary back into list
animals.items() # returns key: value pairs
list(animals.items()) # turns it back into a list

# what if we want a different structure than what we started with
# write a list comprehesnion
[{'letter': key, 'name': value} for key, value in animals.items()]