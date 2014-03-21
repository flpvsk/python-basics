"""D
"""

import sys
import traceback
from pkgutil import walk_packages


def run():
    print("Searching for modules in %r" % sys.argv[1])
    packages_gen = walk_packages([sys.argv[1]], sys.argv[1] + '.')
    for importer, name, is_package in packages_gen:
        if is_package:
            continue
        try:
            module = importer.find_module(name).load_module(name)
            print name, dir(module)
        except:
            print >> sys.stderr, "Error during %r module import!" % name
            traceback.print_exc(None, sys.stderr)


if __name__ == '__main__':
    run()
