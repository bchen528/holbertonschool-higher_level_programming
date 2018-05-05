#!/usr/bin/python3
"""
Multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """multiplies two matrices
    Args:
        m_a (:obj:`list` of :obj:`list` of :obj:`int` or :obj:`float`):
            list of lists of integers or floats
        m_b (:obj:`list` of :obj:`list` of :obj:`int` or :obj:`float`):
            list of lists of integers or floats
    Returns:
        a new matrix containing dot products
    Raises:
        TypeError: if m_a or m_b is not a list, if one element of those
            two lists is not an integer or a float,
            if m_a and m_b are not rectangular
        ValueError: if m_a or m_b is empty, if m_a or m_b can't be multiplied
    """
    new = []
    dp = 0
    flag = 1
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if m_a is None:
        raise ValueError("m_a can't be empty")
    if m_b is None:
        raise ValueError("m_b can't be empty")

    for i in range(len(m_a)):
        inside = []
        for j in range(len(m_b[i])):
            if len(m_a[i]) != len(m_b):
                raise ValueError("m_a and m_b can't be multiplied")
            if type(m_a[i]) is not list and type(m_a[i][j]) is not int\
               and type(m_a[i][j]) is not float:
                raise TypeError("m_a should contain only integers or floats")
            if type(m_b[i]) is not list and type(m_b[i][j]) is not int\
               and type(m_b[i][j]) is not float:
                raise TypeError("m_b should contain only integers or floats")
            if len(m_a[0]) != len(m_a[i]):
                raise TypeError("each row of m_a must "
                                "should be of the same size")
            if len(m_b[0]) != len(m_b[i]):
                raise TypeError("each row of m_b must "
                                "should be of the same size")
            for k in range(len(m_b)):
                temp = m_a[i][k] * m_b[k][j]
                dp += temp
                if k == len(m_b) - 1:
                    inside.append(dp)
                    dp = 0
            if j == len(m_b[i]) - 1:
                new.append(inside)
    return new
