import timeit
import math_functions


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def add_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")

    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)

    return result


def subtract_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")

    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] - mat2[i][j])
        result.append(row)

    return result

def multiply_matrices(mat1, mat2):

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


def transpose_matrix(mat):
    result = []
    for i in range(len(mat[0])):
        row = [mat[j][i] for j in range(len(mat))]
        result.append(row)

    return result


def scalar_multiply_matrix(mat, scalar):
    result = []
    for i in range(len(mat)):
        row = [mat[i][j] * scalar for j in range(len(mat[i]))]
        result.append(row)

    return result


def determinant_matrix(mat):
    if len(mat) != len(mat[0]):
        raise ValueError("Matrix must be square.")

    if len(mat) == 1:
        return mat[0][0]

    det = 0
    for j in range(len(mat[0])):
        minor = [row[:j] + row[j + 1:] for row in mat[1:]]
        cofactor = (-1) ** j * mat[0][j] * determinant_matrix(minor)
        det += cofactor

    return det


def test_python():
    a = factorial(100)
    b = fibonacci(100)
    c = is_prime(1000000000)

    N = 6
    mat1 = [[999] * N for _ in range(N)]
    mat2 = [[879] * N for _ in range(N)]
    k = 3

    add_matrices(mat1, mat2)
    subtract_matrices(mat1, mat2)
    multiply_matrices(mat1, mat2)
    determinant_matrix(mat1)
    transpose_matrix(mat2)
    scalar_multiply_matrix(mat1, k)


def test_cython():
    a = math_functions.factorial(100)
    b = math_functions.fibonacci(100)
    c = math_functions.is_prime(1000000000)

    N = 6
    mat1 = [[999] * N for _ in range(N)]
    mat2 = [[879] * N for _ in range(N)]
    k = 3

    math_functions.add_matrices(mat1, mat2)
    math_functions.subtract_matrices(mat1, mat2)
    math_functions.multiply_matrices(mat1, mat2)
    math_functions.determinant_matrix(mat1)
    math_functions.transpose_matrix(mat2)
    math_functions.scalar_multiply_matrix(mat1, k)


if __name__ == '__main__':
    # Timing the computation of python functions
    t = 10
    time1 = timeit.timeit(stmt=test_python, number=t)
    time2 = timeit.timeit(stmt=test_cython, number=t)

    print(f"Time taken without Cython extension: {time1 / t: .5f}")
    print(f"Time taken with Cython extension: {time2 / t: .5f}")
