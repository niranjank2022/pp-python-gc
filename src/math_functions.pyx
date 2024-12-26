cimport numpy as np
from cython cimport boundscheck, wraparound


# Function to add two matrices
def add_matrices(list mat1, list mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")

    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)

    return result


def subtract_matrices(list mat1, list mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")

    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] - mat2[i][j])
        result.append(row)

    return result

def multiply_matrices(list mat1, list mat2):
    if len(mat1[0]) != len(mat2):
        raise ValueError("Number of columns of the first matrix must equal the number of rows of the second.")

    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            value = 0
            for k in range(len(mat2)):
                value += mat1[i][k] * mat2[k][j]
            row.append(value)
        result.append(row)

    return result

def transpose_matrix(list mat):
    result = []
    for i in range(len(mat[0])):
        row = [mat[j][i] for j in range(len(mat))]
        result.append(row)

    return result

def scalar_multiply_matrix(list mat, double scalar):
    result = []
    for i in range(len(mat)):
        row = [mat[i][j] * scalar for j in range(len(mat[i]))]
        result.append(row)

    return result

def determinant_matrix(list mat):
    if len(mat) != len(mat[0]):
        raise ValueError("Matrix must be square.")

    if len(mat) == 1:
        return mat[0][0]

    det = 0
    for j in range(len(mat[0])):
        minor = [row[:j] + row[j+1:] for row in mat[1:]]
        cofactor = (-1) ** j * mat[0][j] * determinant_matrix(minor)
        det += cofactor

    return det

# Disable bounds checking and wraparound for performance
@boundscheck(False)
@wraparound(False)
def factorial(int n):
    cdef int i
    cdef long long result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(int n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    cdef int a = 0, b = 1, i
    for i in range(n - 1):
        a, b = b, a + b
    return b


def is_prime(int num):
    if num <= 1:
        return False
    cdef int i
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
