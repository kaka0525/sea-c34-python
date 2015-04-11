# Arguments (3 questions)

# Question 1

default_val = 12


def sample1(x=default_val):
    """
    What happens if I try to reassign the default variable?

    Result:
        12 is printed to the console.
        (line 14) - A default variable cannot be reassigned
    """
    return x

default_val = 50

print sample1()


# Question 2


def sample2(**kwargs, *args):
    """
    What happens if I flip the order of the parameters kwargs and args by
    putting kwargs before args?

    Result:
        invalid syntax
        (line 23) - parameters must be in order (*args, **kwargs)

    """
    print("optional arguments are: %s" % unicode(kwargs))
    print("positional arguments are: %s" % unicode(args))

sample2(12, 50, Wilson=3, Sherman=25)


# Question 3


def sample3(*apples, **oranges):
    """
    Can I used a different name for the parameters *args and **kwargs?

    Result:
        Yes, the name of your parameters can be anything so long as *args
        proceeds **kwargs.

    """
    print("positional arguments are: %s" % unicode(apples))
    print("optional arguments are: %s" % unicode(oranges))

sample3(1, 2, 3, 4, 5, team="Seahawks")
