'''
Created on Apr 3, 2014 

@author: arakann 
''' 


def log1(f): 

    def wrapper(*args, **kwargs): 
        try: 
            print ('{}{}'.format(f.__name__, args, kwargs)) 
            result = f(*args, **kwargs) 
            print ('returns {}'.format(result)) 
        except Exception: 
            raise Exception
    return wrapper 




@log1 
def assert_equal(a, b): 
    assert a==b 

@log1 
def args_sum(*args, **kwargs): 
    return sum(kwargs.values()) + sum(args) 


args_sum(2,3)


try:
    assert_equal(1, 2)
except AssertionError as e:
    print ('1!=2: %r' % e.message)