from collections import defaultdict
##  DICTIONARIES
animals = {
    'a': 'aardvark',
    'b': 'bear',
    'c': 'cat', # trailing comma is convention even if its the last item
}
animals

animals['a']
# add a dog
animals['d'] = 'dog'
animals
#update the dict
animals['a'] = 'antelope'
animals # aardvark cahnges to antelope

animals.keys() # 'dict_keys' object, looks like list but immutable
animals.values()
# change dict_keys into list
list(animals.keys())

# access a key thats not present
animals['e']
animals.get('e', 'elephant') # second argument is a default, define if there is none
# return 'none' if you do not give it a default value
len(animals)

# DICTIONARY OF LISTS
animals = {
    'a': ['aardvark', 'antelope'],
    'b': ['bear'],
}

# append bison to b
animals['b'].append('bison')
animals # bison now included

# lets add cat
animals['c'] = ['cat']
#what if we dont know what the key is and we are overwriting something?
if 'c' not in animals:
    animals['c'] = []
animals['c'].append('cat')

##  THE DEFAULT DICT
animals = defaultdict(list)
animals # nothing in it yet

animals['e'].append('elephant')
animals # adds elephant as list value for key 'e'
animals['e'].append('emu')
animals

animals['f']
animals # adds an empty f


