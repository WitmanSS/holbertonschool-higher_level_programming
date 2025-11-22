#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    lastmatrix = []
    for i in matrix:
        arrayininside = []
        for j in i:
            arrayininside.append(j**2)
        lastmatrix.append(arrayininside)
    return lastmatrix
