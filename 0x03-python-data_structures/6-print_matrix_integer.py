#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for syn in matrix:
        for syn2 in syn:
            print("{:d}".format(syn2),
                  end="" if syn[len(syn)-1] == syn2 else " ")
        print("".format())
