#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    m = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
            m += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print()
    return m
