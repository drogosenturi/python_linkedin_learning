from decimal import Decimal, getcontext # importans decimal package
## MORE INTEGERS
int('100')
int('100',2) # after comma, converts it to that base

int('1ab', 16)

# DECIMAL MODULE
getcontext() # returns context object with attributes

#change the settings
getcontext().prec=4

Decimal(1) / Decimal(3) ## accurate to 4 places
getcontext().prec=2 # change to 2
Decimal(1) / Decimal(3) ## accurate to only 2

#float to decimal
Decimal(3.14) ## returns huge number
# if you want it to be perfectly precise then input as string
Decimal('3.14')

## floats are fine most of the time with round function

