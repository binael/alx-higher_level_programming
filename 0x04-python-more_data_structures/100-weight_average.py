#!/usr/bin/python3

def weight_average(my_list=[]):
    """function that returns the weighted average of all integers tuple"""

    tot_weight = 0
    total = 0

    if my_list:
        for score, weight in my_list:
            total += (score * weight)
            tot_weight += weight

        return total/tot_weight
    else:
        return 0
