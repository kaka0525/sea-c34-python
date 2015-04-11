"""
===============================================================================
file: lambda.py
===============================================================================
Programmer: Jeffrey Mendiola
Date: 04/06/2015
Course: SEA-C34: Foundations II: Python
Time: MW 7:00pm - 9:00pm
Instructor: Paul Pham
Task: #15
Description:
     This program has one function that takes one argument.
     When called, it returns a list of n functions, such that each one,
     when called, will return the input value, incremented by an
     increasing number
===============================================================================
"""


def list_increment(n):
    """Returns a list of n functions, such that each one, when called, will
    return the input value, incremented by an increasing number."""
    return [lambda a, b=i: a + b for i in range(n)]

if __name__ == "__main__":
    the_list = list_increment(4)
    print "the_list[0](2) == 2"
    print(the_list[0](2) == 2)
    print "\n"
    print "the_list[1](2) == 3"
    print(the_list[1](2) == 3)
