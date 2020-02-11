import hashlib

key = b"mom"
my_string = "this is a normal string.  nothing to see here.".encode()

for i in range(10):
    hashed = hash(key)
    print(hashed % 8)
