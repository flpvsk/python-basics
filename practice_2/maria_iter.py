from examples_2.utils import print_stars

print_stars() 
print("Dividers practice")

def dividers(x):
    result = [1]
    for i in xrange(2, x/2+1):
        if x%i == 0:
            result.append(i);
    return result

number = input("Please, enter some natural number > ")   

if isinstance(number, int) and number > 0:
    print("{} dividers are: {}".format(number, dividers(number)))  
else:
    print("Entered value is not a natural number")         


print_stars()
print("Booleans practice")

def to_bool(lst):
    booled_list = []
    for el in lst:
        booled_list.append(bool(el))
    return booled_list

lst = [0, 1, '', None, "String", 0.0, 0.234]
print("Initial list: {0}".format(', '.join(str(e) for e in lst)))
print("Booled list: {}".format(', '.join(str(e) for e in to_bool(lst))))
