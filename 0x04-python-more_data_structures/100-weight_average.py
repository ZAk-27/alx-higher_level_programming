#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or my_list is None:
        return 0
    totVal = 0
    weight = 0
    for i in my_list:
        totVal += i[0] * i[1]
        weight += i[1]
    return totVal / weight
