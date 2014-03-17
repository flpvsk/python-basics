import sys
import importlib
from runner import clear_state
from runner import add_test
from runner import run
from runner import failed_tests

if __name__ == '__main__':
    package_name = sys.argv[1]
    module = importlib.import_module(package_name)
    for func in dir(module):
        if func in module.__all__ and not (func.startswith("__") and func.endswith("__")):
            clear_state()
            add_test(getattr(module,func))
            run()
            if len(failed_tests()) != 0:
                sys.exit(1)
            else:
                sys.exit(0)