#!usr/bin/python3
"""Here we would be checking if an object is an instance of 
a class or class that inherits from another class"""


def is_kind_of_class(obj, a_class):
    return (isinstance(obj, a_class))

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))