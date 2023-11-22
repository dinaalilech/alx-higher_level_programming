#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2"""
    return (dict(map((lambda key: (key, a_dictionary[key]*2)), a_dictionary)))
