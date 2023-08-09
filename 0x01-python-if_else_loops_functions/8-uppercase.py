#!/usr/bin/python3
def uppercase(str):
    for z in str:
        if ord(z) in range(97, 123):
            k = ord(z) - 32
        else:
            k = ord(z)
        print("{:c}".format(k), end='')
    print("")
