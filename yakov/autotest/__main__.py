'''
Created on Mar 20, 2014

@author: Java Student
'''
import sys
import importlib
import runner as run


def path_to_module(path):
    #print path
    parts = path.split("\\")
    if len(parts) == 1:
        parts = path.split("/")
    if parts[0] == '':
        parts.pop(0)
    #print parts
    module = ".".join(parts)
    #print module
    return module.replace('.py', '')


tm = importlib.import_module(path_to_module(sys.argv[1]))

#print "Tests are in module: " + tm.__name__


def prepare_tests_to_run():
    run.clear_state()
    for t in tm.__all__:
        run.add_test(getattr(tm, t))
    #print run.pending_tests()


def execute_tests():
    run.run()
    return len(run.failed_tests())

prepare_tests_to_run()
print execute_tests()
