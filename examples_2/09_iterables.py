from examples_2.utils import print_stars

# Strings
print("String:")
for letter in 'word':
    print("  %r" % letter)
print_stars()

# Lists
print("List:")
for el in [1, 2, ['sub-list'], '3']:
    print("  %r" % el)
print_stars()

# Tuples
print("Tuple:")
for el in (1, 'tuple', 2):
    print("  %r" % el)
print_stars()

# Dicts
print("Dict:")
for key in {"key1": 1, 2: 2}:
    print("  %r" % key)
print_stars()

# Iterables unpacking
print("Unpack")
x, y = [1, 2]
print("x, y = [1, 2]       -> x = %r\ty = %r" % (x, y))
x, y = 'xy'
print("x,y = 'xy'          -> x = %r\ty = %r" % (x, y))
x, y = ('v1', 'v2')
print("x, y = ('v1', 'v2') -> x = %r\ty = %r" % (x, y))
print_stars()
