#!/usr/bin/python3

for q in range(0, 9):
    for l in range(q + 1, 10):
        if q != 8:
            print("{:d}{:d}".format(q, l), end=', ')
        else:
            print("{:d}{:d}".format(q, l))
