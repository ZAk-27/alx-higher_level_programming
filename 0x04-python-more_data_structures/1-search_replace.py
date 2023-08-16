#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [numb if not numb == search else replace for numb in my_list]
