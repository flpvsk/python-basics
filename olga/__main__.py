#from console_tests import *
#import console_tests
#cmd example C:\Users\Olga\git\python-basics>C:\Python27\python -m olga olga.console_tests
from runner import runner
import sys
if len(sys.argv) > 1:
    #imports cmd arg as module
    __import__(str(sys.argv[1]), globals={"__name__": __name__})
    
    test_runner = runner()
    #add all tests to runner
    for x in sys.modules[str(sys.argv[1])].__all__:
        #test_runner.add_test(x)
        test_runner.add_test(getattr(sys.modules[sys.argv[1]], x))
    #run tests
    test_runner.run()
    #return result
    if test_runner.failed_tests():
        print(1)
    else:
        print(0)
else:
    print("Please enter tests file name")
