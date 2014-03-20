# -*- coding: utf-8 -*-
from examples_2.utils import print_stars

single_line_byte_string = "single line byte string"
print(single_line_byte_string)
print_stars()

multi_line_byte_string = """Multi
Line
Byte
String"""
print(multi_line_byte_string)
print_stars()

single_line_unicode_string = u"single line unicode string \u263a"
print(single_line_unicode_string)
print_stars()

# search for occurences
print("x in abc? {}".format("x" in "abc"))
print("x in xyz? {}".format("x" in "xyz"))
print_stars()

# string length
print('len("12345"): {}'.format(len("12345")))
print_stars()

# c-style format:
#http://docs.python.org/2/library/stdtypes.html#string-formatting
print('c-style format: %d' % 1.0)
print_stars()

# python-style format:
# http://docs.python.org/2/library/string.html#format-string-syntax

# indexes and slices
my_string = "My String"
print("my_string[0]:      {!r}".format(my_string[0]))
print("my_string[1:3]:    {!r}".format(my_string[1:3]))
print("my_string[:-1]:    {!r}".format(my_string[:-1]))
print("my_string[::2]:    {!r}".format(my_string[::2]))
print("my_string[1:-1:3]: {!r}".format(my_string[1:-1:3]))
print_stars()

# joins
print('", ".join(["a", "b", "c"]): {!r}'.format(", ".join(["a", "b", "c"])))
print_stars()

# more info with help: help(str)
