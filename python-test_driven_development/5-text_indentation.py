#!/usr/bin/python3
"""
Module for text_indentation function
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The input text to be processed

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize variables
    result = ""
    skip_space = False

    # Process each character
    for char in text:
        # Skip space if previous char was delimiter
        if skip_space and char == " ":
            continue

        result += char
        skip_space = False

        # Add two newlines after delimiters
        if char in ".?:":
            result += "\n\n"
            skip_space = True

    # Print result without trailing whitespace
    print(result.strip(), end="")
