#!/usr/bin/python3
"""
Module for text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text to be processed

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove spaces at the beginning and end of each line
    text = text.strip()

    # Replace characters with character + 2 newlines
    for delim in ".?:":
        text = text.replace(delim, delim + "\n\n")

    # Split text into lines
    lines = text.split("\n")

    # Print each line with proper formatting
    for i, line in enumerate(lines):
        if i != len(lines) - 1:
            print(line.strip())
        else:
            print(line.strip(), end="")
