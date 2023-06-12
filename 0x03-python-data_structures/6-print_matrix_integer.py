#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        formatted_row = ""
        for j in i:
            formatted_row += "{:d} ".format(j)
        print(formatted_row.strip())
