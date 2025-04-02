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

    text = text.strip()  # Remove leading and trailing spaces

    i = 0
    while i < len(text):
        # Print current character
        print(text[i], end="")

        # If character is ., ? or :, print two newlines
        if text[i] in ".?:":
            print("\n")
            # Skip spaces after special characters
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
