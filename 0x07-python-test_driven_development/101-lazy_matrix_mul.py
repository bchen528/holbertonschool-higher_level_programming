#!/usr/bin/python3
"""
multiplies two matrices
"""

import numpy
"""
This module contains useful linear algebra operations
"""


def lazy_matrix_mul(m_a, m_b):
    """multiplies two matrices"""
    return numpy.matmul(m_a, m_b)
