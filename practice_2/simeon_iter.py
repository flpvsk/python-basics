list=[]
def dividers(x):
    for i in range(1,x):
        if (x % i) == 0:
            list.append(i)
    print("list of dividers {}\n".format(list))
    return list
 
dividers(10)


lstB=[]
def to_bool(lst):
    for i in lst:
        lstB.append(bool(i))
    print("to_bool{} -> {}".format(lst,lstB))
    return lstB

to_bool([0, 1, '', 'a'])
# [False, True, False, True]