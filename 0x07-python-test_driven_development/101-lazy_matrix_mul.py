#!/usr/bin/python3
"""Defining a function that does matrix mutliplication using NumPy"""
import numpy as mp


def lazy_matrix_mul(m_a, m_b):
    """function that does matrix multiplication

    Args:
        m_a (list of lists of ints/floats): first matrix
        m_b (list of lists of ints/floats): second matrix
    """
    return (mp.matmul(m_a, m_b))
