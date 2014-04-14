from examples_2.utils import print_stars

def sum_args(first_summand, *args, **kwargs):
    sum = first_summand
    for arg in args:
        sum += arg
    for kwargs in kwargs:
        sum += kwargs
    return sum

print_stars()
print("Test 1 - without arguments")
try:
    sum_args()
except TypeError as e:
    print("Exception caught: %r" % e.message)
else:
    print("Failed")

print_stars()
print("Test 2 - 1 object")     
result = sum_args(25)
print("Result: {}".format(result))

print_stars()
print("Test 3 - 2 int objects")
result = sum_args(25, 5)
print("Result: {}".format(result))

print_stars()
print("Test 4 - 3 tuple objects")
result = sum_args((1, 2), (3, 4), (4, 5, 6))
print("Result: {}".format(result))    