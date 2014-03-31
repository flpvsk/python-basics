def assert_equals(a, b):
    assert a == b


def with_msg(msg_format):

    def decorator(f):

        def wrapper(*args, **kwargs):

            try:
                return f(*args, **kwargs)
            except AssertionError as e:
                e.message = msg_format.format(*args, **kwargs)
                raise

        return wrapper

    return decorator



try:
    assert_equals(1, 2)
except Exception as e:
    print 'Without wrap: %r' % e.message


try:
    wrap = with_msg('{} != {}')
    wrapped_assert = wrap(assert_equals)
    wrapped_assert(1, 2)
except Exception as e:
    print 'With wrap: %r' % e.message


@with_msg('{} not in {}')
def assert_in(a, b):
    assert a in b


@with_msg('{} is False')
def assert_true(a):
    assert a


try:
    assert_in(1, [])
except Exception as e:
    print('assert_in(1, []): %r' % e.message)


try:
    assert_true(0)
except Exception as e:
    print('assert_true(0): %r' % e.message)

