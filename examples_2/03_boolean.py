from examples_2.utils import print_stars

boolean = True
# Expressive python
print("boolean is True or False: {}".format(boolean is True or False))

print_stars()

if boolean:
    print("boolean is True")
else:
    # will not get here
    print("boolean is False")

print_stars()

# `and` is same as `&&` in Java, C
if not boolean and boolean:
    # will not get here
    print("False and True is False")

print_stars()

# `or` is same as `||` in Java, C
if not boolean or boolean:
    print("False or True is True")

print_stars()

list1 = []
list2 = []

print("Lists are same:  {}".format(list1 is list2))  # `is` is same as `==` in Java
print("Lists are equal: {}".format(list1 == list2)) # `==` is same as `.equals()` in Java
print(id(list1), id(list2))
print(id(True), id(True))

print_stars()

# In python everything can be cast to True or False
print("Empty String:     {}".format(bool("")))
print("Non-Empty String: {}".format(bool("not empty")))
print("Zero:             {}".format(bool(0)))
print("One:              {}".format(bool(1)))