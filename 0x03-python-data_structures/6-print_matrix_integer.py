#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if len(matrix) == 1:
                break
            print("{}".format(matrix[i][j]), end="")
            if j + 1 < len(matrix):
                print(" ", end="")
        print()
