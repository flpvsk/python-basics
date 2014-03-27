from runner import *
from assertions import *


def my_set_up(f):
    
    def new_set_up(*args, **kwargs):
        print("my_set_up before " & f.__name__)
        try:
            f(*args, **kwargs)
        except:
            pass
        finally:
            pass
    return new_set_up


if __name__ == "__main__":
    my_runner = TestRunnerReporter(VerboseReporter())
    my_runner.add_test(test_assert_equal)
    my_runner.add_test(test_assert_is_none)
    my_runner.add_test(test_assert_not_equal)
    my_runner.run()