def print_my_name():
    print("Andrey")


def print_before_and_after(f):
    def new_f(*args, **kwargs):
        print("Going to %s" % f.__name__)
        try:
            return f(*args, **kwargs)
        finally:
            print("Finished %s" % f.__name__)

    return new_f


new_print_my_name = print_before_and_after(print_my_name)


print_my_name()
# new_print_my_name()


def sum_of_two(x, y):
    return x + y


new_sum_of_two = print_before_and_after(sum_of_two)
sum_of_two(1, 2)
# new_sum_of_two(1, 2)
