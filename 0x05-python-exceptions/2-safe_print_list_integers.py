#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counts = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            counts += 1

    print()
    return (counts)
