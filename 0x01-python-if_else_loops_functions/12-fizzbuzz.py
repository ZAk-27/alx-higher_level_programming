#!/usr/bin/python3
def fizzbuzz():
    for k in range(1, 101):
        if k % 3 == 0 and k % 5 == 0:
            print("FizzBuzzz", end=" ")
        elif k % 3 == 0:
            print("Fizzz", end=" ")
        elif k % 5 == 0:
            print("Buzzz", end=" ")
        else:
            print(k, end=" ")
