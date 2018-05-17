#!/usr/bin/python3
def pascal_triangle(n):
    """returns a list of lists of integers
        representing the Pascal triangle of size n
    Args:
        n(int): size of Pascal triangle
    Returns:
        list of lists of integers representing Pascal triangle
    """
    outer = []
    for i in range(n):
        inner = []
        for j in range(i + 1):
            if j == 0:
                inner.append(1)
            elif j == i:
                inner.append(1)
            else:
                inner.append(outer[i - 1][j - 1] + outer[i - 1][j])
        outer.append(inner)
    return outer
