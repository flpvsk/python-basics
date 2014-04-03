'''
Created on Apr 3, 2014

@author: Java Student
'''
from converter import *


def main():
    print USD._rates
    dollars_10 = money(10, USD)
    print dollars_10.convert_to(RUB)

if __name__ == '__main__':
    main()
