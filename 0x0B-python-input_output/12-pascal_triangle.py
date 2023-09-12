#!/usr/bin/python3
""" pascal triangl f """


def pascal_triangle(n):
    """ fnc """
    if n <= 0:
        return []
    mylist = []
    for i in range(n):
        mylist.append([])
        for j in range(i):
            if len(mylist[i]) == 0:
                mylist[i].append(1)
                continue
            value = mylist[i-1][j-1] + mylist[i-1][j]
            mylist[i].append(value)
        mylist[i].append(1)
    return mylist
