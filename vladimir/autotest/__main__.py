'''
Created on Mar 20, 2014

@author: Java Student
'''
def path_to_module(path_to_module):
    # Unix style path
    parts = path_to_module.split('/')
    if len(parts) == 1:
        # Windows style path
        parts = path_to_module.split('\\')
    parts[-1] = parts[-1].replace('.py', '')
    module = '.'.join(parts[2:])
    return module