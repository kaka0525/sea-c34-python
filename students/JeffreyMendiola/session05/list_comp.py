"""
===============================================================================
file: list_comp.py
===============================================================================
Programmer: Jeffrey Mendiola
Date: 04/06/2015
Course: SEA-C34: Foundations II: Python
Time: MW 7:00pm - 9:00pm
Instructor: Paul Pham
Task: #13 List Comprehensions
Description:
     This program has one function that takes one argument.
     When called, it returns the number of even integers in the given array.
===============================================================================
"""


def count_evens(nums):
    """ Return the number of even integers in the given array. """
    return len([x for x in nums if x % 2 == 0])

if __name__ == "__main__":
    # count evens test
    assert(count_evens([2, 1, 2, 3, 4]) == 3)
    assert(count_evens([2, 2, 0]) == 3)
    assert(count_evens([1, 3, 5]) == 0)
