# Lambdas and Functional Programming (3 questions)

# Question 1


def sample1():
    """
    How do I square a list of numbers using a map?

    Result:
        [1, 4, 9, 16, 25]
    """
    nums = [1, 2, 3, 4, 5]

    def map_func(x):
        return x ** 2

    return map(map_func, nums)

print sample1()

# Question 2


def sample2():
    """
    Will filter() be able to filter out elements that are not integers?

    Result:
        [12, 3]
    """
    lst1 = [12, 3, "Wilson", True]

    return filter(lambda x: not type(x) != int, lst1)

print sample2()

# Question 3


def sample3():
    """
    Can I add up a list of integer values using reduce()?

    Result:
        Total Amount Donated: $5001
    """
    donations = [1000, 1000, 1000, 1000, 1000, 1]

    return reduce(lambda x, y: x + y, donations)

print "Total Amount Donated: $" + str(sample3())
