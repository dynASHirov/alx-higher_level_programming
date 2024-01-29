#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_delete = []
    for ky, val in a_dictionary.items():
        if val == value:
            to_delete.append(ky)

    for ky in to_delete:
        del a_dictionary[ky]

    return a_dictionary
