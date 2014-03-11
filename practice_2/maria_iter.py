from examples_2.utils import print_stars

def dividers(x):
    result = [1]
    for i in xrange(2, x/2+1):
        if x%i == 0:
            result.append(i);
    return result

number = input("Please, enter some natural number > ")   

print_stars() 

if isinstance(number, int) and number > 0:
    print("{} dividers are: {}".format(number, dividers(number)))  
else:
    print("Entered value is not a natural number")         

    