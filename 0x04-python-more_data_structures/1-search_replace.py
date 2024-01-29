#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cop = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            cop.append(replace)
        else:
            cop.append(my_list[i])
    return (cop)
