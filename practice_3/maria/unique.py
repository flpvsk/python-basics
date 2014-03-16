def unique(lst):
    return dict(zip(lst,lst)).keys()

def print_unique(lst):
    print("Source list: {}".format(lst))
    print("Unique list: {}".format(unique(lst)))

print_unique([1, 2, 3, 2, 4])
print_unique([])
print_unique([4])
print_unique([4,3])
print_unique([3,3])