#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_ = []
    a = len(my_list)
    for i in range(a):
        list_.append(my_list[i] % 2 == 0)
    return (list_)
