#!/usr/bin/python3
def squared(element):
    return (element**2)


def square_matrix_simple(matrix=[]):
    new = matrix[:]
    for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                new[i] = list(map(squared, matrix[i]))
    return new
