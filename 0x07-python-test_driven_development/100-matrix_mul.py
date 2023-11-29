#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif any([not isinstance(l, list) for l in m_a]):
        raise TypeError("m_a must be a list of lists")
    elif any([not isinstance(l, list) for l in m_b]):
        raise TypeError("m_b must be a list of lists")
    elif m_a == [] or all([l == [] for l in m_a]):
        raise TypeError("m_a can't be empty")
    elif m_b == [] or all([l == [] for l in m_b]):
        raise TypeError("m_b can't be empty")
    elif any([not isinstance(i, (int, float)) for l in m_a for i in l]):
        raise TypeError("m_a should contain only integers or floats")
    elif any([not isinstance(i, (int, float)) for l in m_b for i in l]):
        raise TypeError("m_b should contain only integers or floats")
    elif any([len(l) != len(m_a[0]) for l in m_a]):
        raise TypeError("each row of m_a must be of the same size")
    elif any([len(l) != len(m_b[0]) for l in m_b]):
        raise TypeError("each row of m_b must be of the same size")
    elif len(m_a) != len(m_b[0]) and len(m_b) != len(m_a[0]):
        raise ValueError("m_a and m_b can't be multiplied")
    if len(m_a) == len(m_b[0]):
        size = len(m_a)
        new_matrix = [[sum([m_a[k][i] * m_b[j][k] for k in range(size)]) for i in range(len(m_a[0]))] for j in range(len(m_b))]
    else:
        size = len(m_b)
        new_matrix = [[sum([m_a[i][k] * m_b[k][j] for k in range(size)]) for j in range(len(m_b[0]))] for i in range(len(m_a))]
    return (new_matrix)
