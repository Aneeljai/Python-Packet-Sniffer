from struct import *

# Store as bytes data
packet_data = pack('iif', 6, 19, 4.73)
print(packet_data)

# How many bytes are needed to store these values
print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# To get it back to normal
original_data = unpack('iif', packet_data)
print(original_data)

# You can also do
print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))
