'''
Created on Mar 9, 2014

@author: ROO
'''
#Straightforward way to get all unique values from the list
def unique1(lst):
    outputList = []
    for el in lst:
        if el not in outputList:
            outputList.append(el)
    print(outputList)

#Another way would be to convert list into a set and after again into a list 
def unique2(lst):
    myset=set(lst)
    print(list(myset))
    
unique1([1,1,4,5,2,2])
unique2([1,1,4,5,2,2])