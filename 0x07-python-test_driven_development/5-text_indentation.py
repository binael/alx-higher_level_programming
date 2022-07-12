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
        raise TypeError("text must be a string")

    flag = False
    for i in text:
        if not flag:
            if not i.strip():
                continue
            flag = True
        print(i, end='')
        if i in ".?:":
            print('\n\n', end='')
            flag = False
