#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for m, p in dict(sorted(a_dictionary.items())).items():
        print("{}: {}".format(m, p))
