##      INTS AND FLOATS
20 / 4 # returns a float for division
4 + 4.0 # returns floats

## if you want it to return an int
int(4 ** 4.0)
# this is called casting

int(8.9)
int(8.99999) ## returns 8 when you cast, does not round, just cuts off decimal

##  if you want to round to nearest int
round(14/3)
round(14/3, 2) # define number of decimals places to round to

# python messes up when you subtract floats
1.2 - 1.0
# if you want it to be more precise:
round(1.2 - 1.0, 2)


