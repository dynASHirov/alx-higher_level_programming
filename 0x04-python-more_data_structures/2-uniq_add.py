#!/usr/bin/python3
def uniq_add(my_list=[]):
    numb = 0
    for element in set(my_list):
        numb += element
    return numb
