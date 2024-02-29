# LISTS
my_list = [1,2,3,4]
print(my_list)

#list of strings
my_list = ['list','of','strings']

#list of mixed data types
my_list = [1,'list',False,[]]

#list of lists with different data types
my_list = [[1,2,3,4],[False,True],[]]

# Length
len(my_list)

#   SETS
my_set = {1,2,3,4,5}
print(my_set)
type(my_set)
len(my_set)

# Every element in a set needs to be unique
my_set = {1,1,2,2}
len(my_set) # only 2 because repeats
print(my_set)

[1,2] == [2,1] # not true cause items are in different order

{1,2,3} == {3,2,1,1,1} # true because order doesnt matter and same length

##  TUPLES

my_tuple = (1,2,3)
len(my_tuple)

(1,2) == (2,1) # false cause order matters

my_list.append(4)
print(my_list) # adds the 4

my_tuple.append(4) # doesn't work cause you cannot append tuples

## why use tuples??
# they are memory efficient
# storing x,y coordinates

##  DICTIONARIES
my_dictionary = {
    'apple': 'A red fruit',
    'bear': 'A scary animal',
    'apple': 'sometimes a green fruit' ## uses this one because it uses the last definition of the item
}

my_dictionary['bear'] # can only have one definition per object

my_list[1]




















