# Built-in exceptions: http://docs.python.org/2/library/exceptions.html

# I
try:
    raise AssertionError()
except AssertionError:
    print('I: In except AssertionError')
except Exception:
    print('I: In except Exception')


# II
try:
    raise AssertionError()
except TypeError:
    print('II: In except TypeError')
except BaseException:
    print('II: In except BaseException')
except Exception:
    print('II: In except Exception')


# III
try:
    raise AssertionError()
except:
    print('III: In empty except')
