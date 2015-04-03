from __future__ import print_function
import sys
import traceback

# 1 Question (2 Written)


def instance_precedence():
    """Do instance attributes supercede class attributes?"""
    class Foo(object):
        size = 4
        color = "red"

        def __init__(self, x, y):
            """Create instance."""
            self.x = x
            self.y = y
            self.size = 10
    bar = Foo(2, 6)
    assert(bar.size == 10)
    print(bar.size)


instance_precedence()
# result: Yes, they do.


def self_test():
    """What happens when I pass self explicitly when creating an instance?"""
    class Foo(object):
        size = 4
        color = "red"

        def __init__(self, x, y):
            """Create instance."""
            self.x = x
            self.y = y
    try:
        bar = Foo(self, 2, 6)
        assert(bar.x == 2)
    except NameError:
        traceback.print_exc(file=sys.stdout)


self_test()
# result: Apparently, this throws a NameError exception. Python seems to
# think that I am referring to a separate global name 'self' when I pass
# it explicitly in this way.
