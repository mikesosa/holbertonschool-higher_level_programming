#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s1 = []
    s2 = []
    s3 = []
    for i in matrix:
        for j in i:
            if len(s1) < 3:
                s1 += [j**2]
                continue
            if len(s2) < 3:
                s2 += [j**2]
                continue
            if len(s3) < 3:
                s3 += [j**2]
                continue
    return [s1, s2, s3]
