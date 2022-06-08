#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_2 = a_dictionary.copy()
    for a in dict_2.keys():
        dict_2[a] *= 2
    return (dict_2)
