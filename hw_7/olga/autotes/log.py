

def log(f):
    def make_std_output(*args, **kwargs):
        s_kwargs = ["{a}={b}".format(a=x, b=kwargs[x]) for x in kwargs]
        s_args = ",".join(str(x) for x in tuple(args) + tuple(s_kwargs))
        try:
            r = " returned {0}".format(f(*args, **kwargs))
        except Exception as e:
            r = "raised {0} with message: '{1}'".format(type(e).__name__, e)
        finally:
            print("{f_name}({args}) call {r}".format(f_name=f.__name__, args=s_args, r=r))
    return make_std_output

@log
def assert_equal(a, b, message="assert_equal error message"):
    assert a == b, "{0} {1} != {2}".format(message, a, b)

@log
def assert_not_equal(a, b, message="assert_not_equal error message"):
    assert a != b, "{0} {1} == {2}".format(message, a, b)

@log
def assert_true(x, message="assert_true error message"):
    assert x, "{0} {1} is False".format(message,x)


if __name__ == "__main__":
    assert_equal(1, 2)
    assert_equal(1,1)
    assert_not_equal(1,"")
    assert_true(True)