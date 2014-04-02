import sys


def log(f):
    def func_descriptor(*args, **kwargs):
        sys.stdout.write("'{}' was called with arguments: {}\n".format(
                            f.__module__ + "." + f.__name__, args, kwargs))
        try:
            result = f(*args, **kwargs)
        except BaseException as e:
            sys.stdout.write("Function failed with exception: {}\n".
                                 format(e.message))
            raise e
        else:
            sys.stdout.write("Function returned value: {}\n".
                                 format(result))
            return result

    return func_descriptor
