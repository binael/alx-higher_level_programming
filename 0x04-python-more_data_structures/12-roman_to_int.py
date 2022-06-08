#!/usr/bin/python3

def roman_to_int(roman_string):
    """Converts roman numerals to integers"""

    roman_dic = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
    symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    total = 0

    if (type(roman_string) != str) or not roman_string:
        return 0

    roman = roman_string.upper()

    for s in roman:
        if s not in symbol:
            return 0

    for i in range(len(roman)):
        if i >= 1:
            list_index = symbol.index(roman[i])

            if roman[i-1] in symbol[:list_index]:
                total -= (2 * roman_dic[roman[i-1]])
                total += roman_dic[roman[i]]
            else:
                total += roman_dic[roman[i]]
        else:
            total += roman_dic[roman[i]]

    return total
