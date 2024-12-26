import math_functions
import numpy as np


def print_matrix(mat):
    print("\n".join(["\t".join(map(str, row)) for row in mat]))


def get_matrix_input():
    rows = int(input(f"Enter the no. of rows: "))
    cols = int(input(f"Enter the no. of columns: "))
    if rows != cols:
        raise ValueError("Matrix must be square for determinant calculation.")
    print(f"Enter the elements of the {rows}x{cols} matrix row by row:")
    mat = []
    for i in range(rows):
        mat.append(list(map(float, input().split())))
    return np.array(mat, dtype=np.float64)


def scientific_calculator():
    print("Welcome to the High-Performance Scientific Calculator!")
    while True:
        print("\nChoose an operation:")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Prime Number Check")
        print("4. Matrix Determinant")
        print("5. Add Matrices")
        print("6. Subtract Matrices")
        print("7. Multiply Matrices")
        print("8. Transpose Matrix")
        print("9. Scalar Multiplication")
        print("10. Program terminated")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter a non-negative integer: "))
            if n < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                result = math_functions.factorial(n)
                print(f"Factorial of {n}: {result}")
        elif choice == 2:
            n = int(input("Enter a positive integer: "))
            if n <= 0:
                print("Input must be a positive integer.")
            else:
                result = math_functions.fibonacci(n)
                print(f"The {n}th Fibonacci number: {result}")
        elif choice == 3:
            num = int(input("Enter an integer: "))
            if math_functions.is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        elif choice == 4:
            try:
                mat = get_matrix_input("Matrix")
                result = math_functions.determinant(mat)
                print(f"Determinant of the matrix: {result}")
            except ValueError as e:
                print(e)
        elif choice == 5:
            mat1 = get_matrix_input("Matrix 1")
            mat2 = get_matrix_input("Matrix 2")
            result = math_functions.add_matrices(mat1, mat2)
            print("Resultant Matrix:")
            print_matrix(result)
        elif choice == 6:
            mat1 = get_matrix_input("Matrix 1")
            mat2 = get_matrix_input("Matrix 2")
            result = math_functions.subtract_matrices(mat1, mat2)
            print("Resultant Matrix:")
            print_matrix(result)
        elif choice == 7:
            mat1 = get_matrix_input("Matrix 1")
            mat2 = get_matrix_input("Matrix 2")
            result = math_functions.multiply_matrices(mat1, mat2)
            print("Resultant Matrix:")
            print_matrix(result)
        elif choice == 8:
            mat = get_matrix_input("Matrix")
            result = math_functions.transpose_matrix(mat)
            print("Transposed Matrix:")
            print_matrix(result)
        elif choice == 9:
            mat = get_matrix_input("Matrix")
            scalar = float(input("Enter the scalar value: "))
            result = math_functions.scalar_multiply_matrix(mat, scalar)
            print("Resultant Matrix after Scalar Multiplication:")
            print_matrix(result)
        elif choice == 10:
            print("Exiting Matrix Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the calculator
if __name__ == "__main__":
    scientific_calculator()
