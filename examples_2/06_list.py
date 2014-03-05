from examples_2.utils import print_stars

empty_list = []
non_empty_list = [1, 'string', 3.0]

# Lists are mutable
print("Before append(4):   %r" % non_empty_list)
non_empty_list.append(4)
print("After append(4):    %r" % non_empty_list)
non_empty_list.insert(0, 0)
print("After insert(0, 0): %r" % non_empty_list)
non_empty_list.pop(1)
print("After pop(1):       %r" % non_empty_list)
non_empty_list[0] = "new 0"
print("After set element:  %r" % non_empty_list)
print_stars()

# Lists are indexed (starting from 0)
print("non_empty_list[1]:        %r" % non_empty_list[1])
print("non_empty_list[1:-1]:     %r" % non_empty_list[1:-1])
print("Slice and List are not same objects: %r" % (
       non_empty_list is not non_empty_list[:]))
print_stars()

# Lists algebra
print("[1, 2] + [3, 4] = %r" % ([1, 2] + [3, 4]))
print("[1] * 4 =         %r" % ([1] * 4))
print_stars()

# List comprehensions
list_0 = [el for el in [1, 2, 3, 4]]
list_map = [2 ** el for el in [1, 2, 3, 4]]
list_filter = [el for el in [1, 2, 3, 4] if el % 2 == 0]
print("[el for el in [1, 2, 3, 4]] =                %r" % list_0)
print("[2 ** el for el in [1, 2, 3, 4]] =           %r" % list_map)
print("[el for el in [1, 2, 3, 4] if el %% 2 == 0] = %r" % list_filter)
print_stars()

# for loop
for el in [1, "string", 3.0, object()]:
    print("In for loop, element is %r" % el)
print_stars()

# classical for loop
for i in xrange(11):
    print("i = %r" % i)
print_stars()

# more info on lists: help(list)
