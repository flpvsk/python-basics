from examples_2.utils import print_stars

def divide(a, b):
    try:
        result = a/b
    except Exception:
        return (False, None)
    else:
        return (True, result)

def print_division_result(a, b):
    print_stars()
    print("Trying to divide '{}' by '{}'".format(a, b))
    print("Result: '{}'".format(divide(a,b)))

print_division_result(1, 0)
print_division_result([], 4)
print_division_result(4, 2)
