#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
dict/set lab solutions: Chris' version.
"""

# Create a dictionary containing "name", "city", and "cake" for
# "Chris" from "Seattle" who likes "Chocolate".


d = {"name": u"Chris",
     u"city": "Seattle",
     u"cake": "chocolate"}

# Display the dictionary.
print d

# or something fancier, like:
print "{name} is from {city}, and likes {cake} cake.".format(**d)


# Delete the entry for "cake".
# Display the dictionary.

del d["cake"]

print d

# Add an entry for "fruit" with "Mango" and display the dictionary.

d[u'fruit'] = 'Mango'

print d

# Display the dictionary keys.

print d.keys()

# Display the dictionary values.

print d.values()

# Display whether or not "cake" is a key in the dictionary (i.e. False) (now).

print 'cake' in d

# Display whether or not "Mango" is a value in the dictionary.

print "Mango" in d.values()

# Using the dict constructor and zip, build a dictionary of numbers
# from zero to fifteen and the hexadecimal equivalent (string is fine).

nums = range(16)
hexes = []
for num in nums:
    hexes.append(hex(num))

hex_dict = dict(zip(nums, hexes))

print hex_dict


# Using the dictionary from item 1: Make a dictionary using the same keys
# but with the number of 'a's in each value.

a_dict = {}
for key, val in d.items():
    a_dict[key] = val.count('a')
print a_dict


# replacing the values:

for key, val in d.items():
    d[key] = val.count('a')
print d

# Create sets s2, s3 and s4 that contain numbers from zero through
# twenty, divisible 2, 3 and 4.
# Display the sets.

s2 = set()
s3 = set()
s4 = set()
for i in range(21):
    if not i % 2:
        s2.add(i)
    if not i % 3:
        s3.add(i)
    if not i % 4:
        s4.add(i)

print s2
print s3
print s4


# Display if s3 is a subset of s2 (False)

print s3.issubset(s2)

# and if s4 is a subset of s2 (True).

print s4.issubset(s2)

# Create a set with the letters in ‘Python’ and add ‘i’ to the set.

s = set(u'Python')
s.add('i')

print s

# maybe:
s = set(u'Python'.lower())  # that wasn't specified...
s.add('i')

# Create a frozenset with the letters in ‘marathon’

fs = frozenset(u'marathon')

# display the union and intersection of the two sets.

print "union:", s.union(fs)
print "intersection:", s.intersection(fs)

# not that order doesn't matter for these:

print "union:", fs.union(s)
print "intersection:", fs.intersection(s)
