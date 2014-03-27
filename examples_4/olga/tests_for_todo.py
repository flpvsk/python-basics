from examples_4.todo import *

# clear() -> items() empty tuple
def test1():
    clear()
    assert isinstance(items(), tuple) and len(items()) == 0, "tets 1 failed"

# + "Sandwich" , items()  "pending".
def tets2():
    clear()
    add('Sandwich')
    assert len(items()) == 1 and items()[0][1] == PENDING, "test2 failed"

def test3():
    clear()
    assert add('Sandwich') == 0, "test 3 failed"

def test4():
    clear()
    assert add('Sandwich') == 0 and add('Sandwich') == 0 and len(items()) == 1, "test 4 failed"

def test5():
    try:
        add()
    except:
        pass
    else:
        raise Exception("test 5 failed")

def test6():
    clear()
    i = add('Sandwich')
    assert status_by_index(i) == PENDING, "tets 6 failed"
    mark_completed_by_index(i)
    assert status_by_index(i) == COMPLETED, "test 6 failed"

def test7():
    clear()
    txt = 'Sandwich'
    add(txt)
    assert status_by_text(txt) == PENDING, "tets 6 failed"
    mark_completed_by_text(txt)
    assert status_by_text(txt) == COMPLETED, "test 6 failed"    

test1()
tets2()
test3()
test4()
test5()
test6()
test7()