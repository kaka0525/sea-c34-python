def subclass_init():
    """Can a subclass have it's own init values?
    """

    class Animal(object):

        def __init__(self, name, sound):
            self.name = name
            self.sound = sound

    class Dog(Animal):

        def __init__(self, ears, eyes):
            self.ears = ears
            self.eyes = eyes

    chihuahua = Dog(2, 2)

    print(chihuahua.ears, chihuahua.eyes)

subclass_init()


def create_instance_of_subclass_with_init_value_from_superclass():
    """Can I create an instance of a sublcass passing the init \
    values of the superclass?
    """
    class Animal(object):

        def __init__(self, name, sound):
            self.name = name
            self.sound = sound

    class Dog(Animal):

        def __init__(self, ears, eyes):
            self.ears = ears
            self.eyes = eyes

    chihuahua = Dog("Bowser", "Woof", 2, 2)
    print(chihuahua.name)  # Returns error
