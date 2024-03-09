## convert hexadecimal to decimal
# hexadecimal is base 16

##  Write a function that converts a string hexadecimal
##  into an integer decimal without using int class

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
##  MY SOLUTION
def hexToDec(hexNum):
    if hexNum in hexNumbers and len(hexNum) == 1:
        return 1 * hexNumbers[hexNum]
    if len(hexNum) == 2 and hexNum[0] in hexNumbers and hexNum[1] in hexNumbers:
        return (16 * hexNumbers[hexNum[0]]) + (hexNumbers[hexNum[1]])
    if len(hexNum) == 3 and hexNum[0] in hexNumbers and hexNum[1] in hexNumbers and hexNum[2] in hexNumbers:
        return (256 * hexNumbers[hexNum[0]]) + (16 * hexNumbers[hexNum[1]]) + (hexNumbers[hexNum[2]])
    else:
        return None
## EASIER WAY TO CHECK IF ALL CHARACTERS ARE IN THE DICTIONARY
def hexToDec(hexNum):
    for i in hexNum:
        if i not in hexNumbers:
            return None
    if len(hexNum) == 1:
        return 1 * hexNumbers[hexNum]
    if len(hexNum) == 2:
        return (16 * hexNumbers[hexNum[0]]) + (hexNumbers[hexNum[1]])
    if len(hexNum) == 3:
        return (256 * hexNumbers[hexNum[0]]) + (16 * hexNumbers[hexNum[1]]) + (hexNumbers[hexNum[2]])


hexToDec('A')
hexToDec('0')
hexToDec('1B')
hexToDec('3C0')
hexToDec('A6G')
hexToDec('ZZTOP')
