from examples_2.utils import print_stars

def unique(lst):
    seen = set()
    return [el for el in lst if el not in seen and not seen.add(el)]
 
lst = [1, 2, 1, 3, 4, 3, 3, 3]
print("Initial list: {}".format(lst))
print("List with unique elements: {}".format(unique(lst)))


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
