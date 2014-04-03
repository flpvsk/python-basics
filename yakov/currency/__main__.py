'''
Created on Apr 3, 2014

@author: Java Student
'''
from converter import currency
from converter import money
from converter import CURRENCIES


def main():
    usd = currency(CURRENCIES[2])
    rub = currency(CURRENCIES[0])
    print usd._rates
    dollars = money(10, usd)
    print dollars.convert_to(rub)

if __name__ == '__main__':
    main()
