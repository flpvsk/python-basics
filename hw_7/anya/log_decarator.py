'''
Created on Apr 3, 2014 

@author: arakann 
''' 


def log1(f): 

    def wrapper(*args, **kwargs): 
        try: 
            print ('{}{}'.format(f.__name__, args, kwargs)) 
            result = f(*args, **kwargs) 
        except Exception as e: 
            print ('Function has failed with Exception {}'.format(e.message)) 
        finally: 
            print ('returns {}'.format(result)) 
    return wrapper 




@log1 
def assert_equal(a, b): 
    #assert a == b 
    raise Exception 


@log1 
def args_sum(*args, **kwargs): 
    return sum(kwargs.values()) + sum(args) 


args_sum(1,2) 
assert_equal(1, 1) 

