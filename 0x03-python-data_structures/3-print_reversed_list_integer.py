#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    t = len(my_list)
    for i in my_list[t::-1]:
        print("{:d}".format(i))
