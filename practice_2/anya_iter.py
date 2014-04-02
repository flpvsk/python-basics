'''
Created on Mar 9, 2014

@author: ROO
'''
from examples_2.utils import print_stars

def dividers(x):
    i=1
    Result=[]
    while i <= x:
        if x%i == 0:
            Result.append(i)
            i=i+1
        else:
            i +=1
    return Result
n=raw_input('Please input a figure')
print (dividers(int(n)))

print_stars()

def to_bool(lst):
    bool_list = [bool(el) for el in lst]
    return bool_list
print ("Bool representation of ['',1,1.5,'anya',0] :  %r" %to_bool(['',1,1.5,'anya',0]))
 


            
