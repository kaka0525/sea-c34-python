# encoding=utf8

"""
===============================================================================
file: dict_comp.py
===============================================================================
Programmer: Jeffrey Mendiola
Date: 04/06/2015
Course: SEA-C34: Foundations II: Python
Time: MW 7:00pm - 9:00pm
Instructor: Paul Pham
Task: #14 Dictionary and Set Comprehensions
Description:

===============================================================================
"""

tommy_prefs = {u"name": u"Tommy",
               u"city": u"Los Angeles",
               u"cake": u"cheese",
               u"fruit": u"watermelon",
               u"salad": u"steak",
               u"pasta": u"mac-n-cheese"}

print "\n\n"

# Item 1
print "Item 1:"
print "> Print the dict by passing it to a string format method.\n"
print(u"""{name} is from {city}, and he likes {cake} cake, {fruit} fruit,
{salad} salad, and {pasta} pasta.""".format(**tommy_prefs))

print "\n\n"

# Item 2
print "Item 2:"
print """> Using a list comprehension, build a dictionary of numbers from zero
to fifteen and the hexadecimal equivalent (string is fine).\n"""
nums_list = [x for x in range(16)]
hexa_list = [hex(x) for x in range(16)]
nums_dict = dict(zip(nums_list, hexa_list))
print nums_dict

print "\n\n"

# Item 3
print "Item 3:"
print "> Do the previous entirely with a dict comprehension.\n"
nums_dict_comp = {num: hex(num) for num in range(16)}
print nums_dict_comp

print "\n\n"

# Item 4
print "Item 4:"
print """> Using the dictionary from item 1: Make a dictionary using the same keys
but with the number of ‘a’s in each value.\n"""
# make copy of item 1 dictionary
tommy_copy = tommy_prefs.copy()
# make string values lower case
tommy_copy = {x: tommy_copy[x].lower() for x in tommy_copy}
# make values the number of a's in each value
tommy_copy = {x: tommy_copy[x].count('a') for x in tommy_copy}
print tommy_copy

print "\n\n"

# Item 5
print "Item 5:"
print """> Create sets s2, s3 and s4 that contain the numbers from zero through
twenty that are divisible 2, 3 and 4.\n"""
s2 = {x for x in range(21) if x % 2 == 0}
print s2
print "\n"

s3 = {x for x in range(21) if x % 3 == 0}
print s3
print "\n"

s4 = {x for x in range(21) if x % 4 == 0}
print s4
print "\n"

print """> do it all as a one-liner by nesting a set comprehension
inside a list comprehension.\n"""
s2, s3, s4 = [{x for x in range(21) if x % y == 0} for y in range(2, 5)]
print s2
print s3
print s4

print "\n\n"
