#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """def documnt"""
    if list_of_integers:
        lfi = 0
        k = len(list_of_integers) - 1
        while lfi < k:
            m = (lfi + k) // 2
            if list_of_integers[m] > list_of_integers[m + 1]:
                k = m
            else:
                lfi = m + 1
        return list_of_integers[lfi]
