"""
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

"""


def sorta_sum(a, b):
    sumOfTwo = a + b
    return 20 if 19 >= sumOfTwo >= 10 else sumOfTwo
