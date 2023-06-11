#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    t = len(my_list) - 1
    for i in range(t, -1, -1):
        print("{0}".format(my_list[i]))
