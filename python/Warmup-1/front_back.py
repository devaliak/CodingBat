"""
Given a string, return a new string where the first and last chars have been exchanged.

"""


def front_back(str):
    return str[-1] + str[1:-1] + str[0]
