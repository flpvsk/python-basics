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

def divide (a,b):
    try:
        Result=a/b
        print [True, Result]
    except ZeroDivisionError:
        print [False, None]
        
divide(1,0)
divide(42,21)

def wc(s): 
    numSymb=len(s) 
    numWords=len(s.split()) 
    numStr=len(s.split("\n")) 
    Result={'symbols':numSymb, 'words':numWords, 'strings':numStr} 
    return Result 
    
print wc('''This is just a little samba 
With all the typical drama 
Feel the rhythm of the conga (come on) 
This is just a little samba''')
