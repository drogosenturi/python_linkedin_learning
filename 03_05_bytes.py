## behind the scenes, rarely manipulated
## used for streaming files

bytes(4) # created an empty byte object 4 bytes long
# 8 bits to a byte
emojibytes = bytes('red', 'utf-8')
emojibytes
emojibytes.decode('utf-8')

## byte data to modify
emojibytes = bytearray('emoji', 'utf-8')

## look into this later if needed


