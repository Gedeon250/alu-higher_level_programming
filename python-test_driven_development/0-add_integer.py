#!/usr/bin/python3
"""
This module contains a function that adds two integers.
The function accepts two parameters and returns their sum.
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.
    Args:
        a: first number (integer or float)
        b: second number (integer or float), defaults to 98
    Returns:
        The addition of a and b as an integer
    Raises:
        TypeError: If a or b is not an integer or float
        OverflowError: If result exceeds maximum integer size
    """
    # Check if a is an integer or float, but not bool
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")

    # Check if b is an integer or float, but not bool
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    # Check for NaN
    if isinstance(a, float) and a != a:  # NaN check
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and b != b:  # NaN check
        raise ValueError("cannot convert float NaN to integer")

    try:
        # Cast float numbers to integers
        a = int(a)
        b = int(b)

        # Perform addition and check for overflow
        result = a + b
        return result
    except OverflowError:
        raise OverflowError("result too large for integer")
