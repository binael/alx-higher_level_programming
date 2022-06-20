#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_list = []

    if list_length <= 0:
        print("out of range")
        return my_list

    for i in range(list_length):
        element = 0
        try:
            a = my_list_1[i] / my_list_2[i]
            element = round(a, 1)
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            my_list.append(element)

    return my_list
