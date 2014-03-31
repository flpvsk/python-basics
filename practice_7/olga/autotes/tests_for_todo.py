from examples_4.todo import *
import functools
from runner import *

def set_up():
    print("set up")
    #assert False, "set_up error"
    clear()

def tear_down():
    print("tear down")
    #assert False, "tear_down error"
    
def with_set_up(set_up_func):
    def my_set_up(test):
        @functools.wraps(test)
        def wrapper(*args, **kwargs):
            set_up_func()
            test()
        return wrapper
    return my_set_up

def with_tear_down(tear_down_func):
    def decorate_tdf(test):
        @functools.wraps(test)
        def wrapper(*args, **kwargs):
            try:
                test()
            finally:
                tear_down_func()            
        return wrapper
    return decorate_tdf

# clear() -> items() empty tuple
@with_set_up(set_up)
@with_tear_down(tear_down)
def test1():
    print("test")
    #assert isinstance(items(), tuple) and len(items()) == 0, "tets 1 failed"
    assert False

# + "Sandwich" , items()  "pending".
@with_set_up(set_up)
@with_tear_down(tear_down)
def test2():

    add('Sandwich')
    assert len(items()) == 1 and items()[0][1] == PENDING, "test2 failed"

@with_set_up(set_up)
@with_tear_down(tear_down)
def test3():
    assert add('Sandwich') == 0, "test 3 failed"

@with_set_up(set_up)
@with_tear_down(tear_down)
def test4():
    assert add('Sandwich') == 0 and add('Sandwich') == 0 and len(items()) == 1, "test 4 failed"

@with_set_up(set_up)
@with_tear_down(tear_down)
def test5():
    try:
        add()
    except:
        pass
    else:
        raise Exception("test 5 failed")

@with_set_up(set_up)
@with_tear_down(tear_down)
def test6():

    i = add('Sandwich')
    assert status_by_index(i) == PENDING, "tets 6 failed"
    mark_completed_by_index(i)
    assert status_by_index(i) == COMPLETED, "test 6 failed"

@with_set_up(set_up)
@with_tear_down(tear_down)
def test7():
    txt = 'Sandwich'
    add(txt)
    assert status_by_text(txt) == PENDING, "tets 6 failed"
    mark_completed_by_text(txt)
    assert status_by_text(txt) == COMPLETED, "test 6 failed"    


if __name__ == "__main__":
    my_runner = TestRunnerReporter(VerboseReporter())
    my_runner.add_test(test1)
    my_runner.add_test(test2)
    my_runner.add_test(test3)
    my_runner.add_test(test4)
    my_runner.add_test(test5)
    my_runner.add_test(test6)
    my_runner.add_test(test7)
    my_runner.run()
    