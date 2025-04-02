#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix
    with elements rounded to 2 decimal places.
    """
    # Validate the matrix
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(element, (int, float)) for row in matrix for element in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each row of the matrix has the same size
    if len({len(row) for row in matrix}) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    # Validate the divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Perform the division and round to 2 decimal places
    return [[round(element / div, 2) for element in row] for row in matrix]

