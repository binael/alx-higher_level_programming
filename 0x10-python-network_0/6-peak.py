"""A program that finds the maximum number in a list
Using divide and conquer algorithm with log(n)
"""

def find_peak(list_of_integers):
    if not (isinstance(list_of_integers, list)):
        return None

    size = len(list_of_integers)

    if size == 0:
        return None
    if size == 1:
        return list_of_integers[0]
    upper = size - 1
    lower = 0
    mid = size / 2

    
