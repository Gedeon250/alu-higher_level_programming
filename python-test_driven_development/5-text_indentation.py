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

    i = 0
    while i < len(text):
        # Skip leading spaces at start of line
        while i < len(text) and text[i] == ' ':
            i += 1
            
        # Print current character
        if i < len(text):
            print(text[i], end="")
            
        # Handle delimiters
        if i < len(text) and text[i] in ".?:":
            print("\n")
            # Skip spaces after delimiter
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
