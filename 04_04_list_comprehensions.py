##  LIST COMPREHENSIONS
mylist = [1,2,3,4,5]
[2*item for item in mylist] # this is a 'list comprehension'
# surround with square bracks and it will iterate over each item
# in the list

# LIST COMPREHENSION WITH FILTERS
mylist = list(range(100)) # list of 0 to 99
filteredList = [item for item in mylist if item % 10 == 0] # modulus gives you division with no remainder
filteredList # reports 0 to 90 by 10s
filteredList = [item for item in mylist if item % 10 < 3]
print(filteredList) # gives first 3 numbers of each sequence

##  LIST COMPREHENSIONS WITH FUCNTIONS
mystring = 'my name is nik. i live in chicago'
mystring.split('.') # split into 2 sentences
mystring.split() # splits on spaces by default

# get rid of the period
def cleanWord(word):
    return word.replace('.','').lower() # chaining functions, replace and lower

[cleanWord(word) for word in mystring.split()] 
# function removes period and split splits by spaces

[cleanWord(word) for word in mystring.split() if len(cleanWord(word)) < 3]
# only returns strings < len 3 and splits/cleans them 

##  NESTED LIST COMPREHENSION
[[cleanWord(word) for word in sentence.split()] for sentence in mystring.split('.')]
# outputs a list of lists where each list is split and cleaned.




