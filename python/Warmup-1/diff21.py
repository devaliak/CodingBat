"""
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
"""


def diff21(n):
    diff = abs(21 - n)
    return diff if n <= 21 else 2 * diff
