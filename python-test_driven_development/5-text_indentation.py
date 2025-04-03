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

    text = text.strip()  # Strip leading/trailing spaces
    result = ""  # Initialize a result string

    i = 0
    while i < len(text):
        char = text[i]
        if char in ".?:":  # Special characters that need new lines
            result += char + "\n\n"  # Append character with two newlines
            i += 1
            # Skip consecutive spaces after special characters
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            result += char
            i += 1

    print(result.strip())  # Print the final result, stripped of extra spaces
