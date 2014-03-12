'''
Created on Mar 12, 2014

@author: ROO
'''

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
