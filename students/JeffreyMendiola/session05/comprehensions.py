# Comprehensions (3 questions)

# Question 1


def sample1():
    """
    How do I print a list using list comprehension?

    Result:
        [0, 4, 16]
    """
    return [x ** 2 for x in range(6) if x % 2 == 0]

print sample1()

# Question 2


def sample2():
    """
    Can I create a list of tuples using list comprehension?

    Result:
        Yes,

        [(0, 0), (1, 10), (2, 20), (3, 30), (4, 40), (5, 50),
        (6, 60), (7, 70), (8, 80), (9, 90), (10, 100)]
    """
    return [(x, x * 10) for x in range(11)]

print sample2()


# Question 3


def sample3():
    """
    Can I combine lists into one using list comprehension?

    Result:
        Yes,

        ['Russell', 'Marshawn', 'Jimmy', 'Richard', 'Earl', 'Kam']

    """
    seahawks = [["Russell", "Marshawn", "Jimmy"], ["Richard", "Earl", "Kam"]]
    return [player for team in seahawks for player in team]

print sample3()
