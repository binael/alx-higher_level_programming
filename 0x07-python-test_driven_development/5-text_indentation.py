#!/usr/bin/python3
"""Text indentations function"""


def text_indentation(text):
    """Prints a text with two new lines after 
    special characters
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.

    """
    if type(text) is not str:
        raise TypeError("text must be string")
    for i in text:
        print(i, end='')
        if i in ".?:":
            print('\n\n', end='')
