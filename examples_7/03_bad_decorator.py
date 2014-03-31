def bad_decorator(f):

    def new_f():
        pass


    return new_f


@bad_decorator
def sum_of_two(x, y):
    return x + y


sum_of_two(1, 2)
