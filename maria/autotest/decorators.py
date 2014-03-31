import sys

def with_set_up(set_up_func):

    def decorator(test):

        def wrapper():
            set_up_func()
            test()

        inherit_attrs(test, wrapper)
        return wrapper

    return decorator


def with_tear_down(tear_down_func):

    def decorator(test):

        def wrapper():
            try:
                test()
            finally:
                tear_down_func()

        inherit_attrs(test, wrapper)
        return wrapper

    return decorator


def inherit_attrs(source, target):
    inherited_attrs = ["__name__", "__module__", "im_class"]
    for attr in inherited_attrs:
            try:
                setattr(target, attr, getattr(source, attr))
            except:
                pass



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
