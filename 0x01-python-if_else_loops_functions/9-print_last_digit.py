#!/usr/bin/python3
def print_last_digit(numb):
    lastdigit = abs(numb) % 10
    print(lastdigit, end="")
    return lastdigit
