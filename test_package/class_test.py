'''
Created on 20 Mar 2014

@author: paraiva
'''


class template(object):
    def __init__(self, name):
        self.name = name


def print_name():
    instance = template('fuflo')
    print instance.name

print_name()
