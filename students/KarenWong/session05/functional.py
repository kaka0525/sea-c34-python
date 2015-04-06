#  Can you put lambda in a tuple?
t = (lambda x, y: x + y,)
print t[0](3, 4)  # Yes


#  Can you use "reduce" on tuples?

reduce(lambda x, y: x + y, t)

t = (2, 4, 6, 8, 10)  # Yes


#  Can you use "map" on tuples?
l = [1, 2, 3, 4, 5]


def tuple_map(x):
    return x * 2

map(tuple_map, l)  # Yes
