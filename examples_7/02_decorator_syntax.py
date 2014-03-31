def print_before_and_after(f):
    def new_f(*args, **kwargs):
        print("Going to %s" % f.__name__)
        try:
            return f(*args, **kwargs)
        finally:
            print("Finished %s" % f.__name__)

    return new_f


# def sum_of_two(x, y):
#     return x + y
#
#
# new_sum_of_two = print_before_and_after(sum_of_two)


@print_before_and_after
def sum_of_two_with_decorator(x, y):
    return x + y


sum_of_two_with_decorator(1, 2)
