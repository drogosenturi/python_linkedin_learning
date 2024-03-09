##  Casting Booleans
bool(1)

bool(0)

bool(-1)
# Anything except bool(0) is TRUE
bool(1j)

## STRINGS ARE TRUE if something contained
bool('True')
bool('False') ## still true
bool('') ## false cause nothing here
# boolean always true if something contained
bool([1,2])

mylist = [1,2]
if mylist:
    print('mylist has some values in it')

a = 5
b = 5
if a - b:
    print('a and b are not equal')
## prints nothing cause false
    
a == b

## LOGIC

weatherIsNice = False
haveUmbrella = True

if not haveUmbrella or weatherIsNice:
    print('stay inside')
else:
    print('go for a walk')
    ## currently messed up, wrong logic because of imaginary parentheses around have umbrella

if not haveUmbrella and not weatherIsNice:
    print('stay inside')
else:
    print('go for a walk')

## i would write it like this
if haveUmbrella or weatherIsNice:
    print('walk')
else:
    print('stay in')