import functools


def with_set_up(set_up_func):

    def decorator(test):

        @functools.wraps(test)
        def wrapper():
            set_up_func()
            test()

        return wrapper

    return decorator


def with_tear_down(tear_down_func):

    def decorator(test):

        @functools.wraps(test)
        def wrapper():
            try:
                test()
            finally:
                tear_down_func()

        return wrapper

    return decorator


def log(f):
    def func_descriptor(*args, **kwargs):
        print "'{}.{}' was called with arguments: {}".format(
                            f.__module__, f.__name__, args, kwargs)
        try:
            result = f(*args, **kwargs)
        except BaseException as e:
            print "Function failed with exception: {}".format(e.message)
            raise e
        else:
            print "Function returned value: {}".format(result)
            return result

    return func_descriptor
