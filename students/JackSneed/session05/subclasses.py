# Question 1

"""Can a I add an instance with a subclass?"""
class Build(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Build("I think", " I got it!")

class NewBuild(Build):
    def __init__(self, name):
        self.name = name

b = NewBuild("Jack")

if __name__ == '__main__':
    print("My name is {} and {}{}.".format(b.name, p.x, p.y))

# Question 2

"""Can I overwrite parent class objects in a child class"""
class parent(object):

    home = "two-story"
    car = "black"

class child(parent):

    car = "blue"

if __name__ == '__main__':
    print("My parents have a {} home. They drive a {} car and mine is {}"
           .format(parent.home, parent.car, child.car))

# Question 3

