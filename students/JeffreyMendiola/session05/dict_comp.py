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

# 1. Print the dict by passing it to a string format method
print(u"""{name} is from {city}, and he likes {cake} cake, {fruit} fruit,
{salad} salad, and {pasta} pasta.""".format(**tommy_prefs))

# 2. Using a list comprehension, build a dictionary of numbers from zero to
#    fifteen and the hexadecimal equivalent (string is fine).
nums_list = [x for x in range(16)]
hexa_list = [hex(x) for x in range(16)]
nums_dict = dict(zip(nums_list, hexa_list))

# 3. Do the previous entirely with a dict comprehension – should be a one-liner
nums_dict_comp = {num: hex(num) for num in range(16)}

# 4. Using the dictionary from item 1: Make a dictionary using the same keys
#    but with the number of ‘a’s in each value. You can do this either by
#    editing the dict in place, or making a new one. If you edit in place, make
#    a copy first!

# make copy of item 1 dictionary
tommy_copy = tommy_prefs.copy()
# make string values lower case
tommy_copy = {x: tommy_copy[x].lower() for x in tommy_copy}
# make values the number of a's in each value
tommy_copy = {x: tommy_copy[x].count('a') for x in tommy_copy}

# 5. Create sets s2, s3 and s4 that contain the numbers from zero through
#    twenty that are divisible 2, 3 and 4.

#    a. Do this with one set comprehension for each set.
#    b. What if you had a lot more than 3? – Don’t Repeat Yourself (DRY)
#       - create a sequence that holds all three sets
#       - loop through that sequence to build the sets up – so no repeated code
#    c. Extra credit: do it all as a one-liner by nesting a set comprehension
#       inside a list comprehension. (OK, that may be getting carried away!)
