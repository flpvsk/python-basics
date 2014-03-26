'''
Created on 23 march 2014
@author: ROO
'''



from examples_4.todo import *


def test_clear_method():
    clear()
    items()
    if items() != ():
        return 'Tuple is not empty as was expected'


def add_into_empty_list_test():
    clear()
    add('Sandwich')
    result_tuple = items()
    print result_tuple
    if result_tuple != (('Sandwich', 'pending'),):
        return "Values in tuple are not correct"


def index_test():
    clear()
    add('Sandwich')
    result_index=add('Sandwich')
    if result_index != 0:
        return "Index is not correct"


def add_2_identical_tasks(task):
    add(task)
    add(task)
    result_tuple=items()
    if result_tuple != ((str(task), 'pending'),):
        return "Values in tuple are not correct"


def empty_desc_test():
    try:
        add('')
    except ValueError:
        return "Empty decription is not valid"
    else:
        assert False, "Test failed: ValueError exception should be thrown"


def test_status_by_index_pending(desc):
    clear()
    index = add(desc)
    if status_by_index(index) != "pending":
        return "Status is incorrect"
    
def test_status_by_index_completed(desc):
    clear()
    index = add(desc)
    mark_completed_by_text(desc)
    if status_by_index(index) != "completed":
        return "Status is incorrect"
