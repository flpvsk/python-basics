def bad_decorator(f):

    def new_f(*args, **kwargs):
        print ('Starting %s' % new_f.__name__)
        try:
            f(*args, **kwargs)
        except: 
            Exception
        finally:
            print ('Finishing %s' % new_f.__name__)
        
            
        pass


    return new_f


@bad_decorator
def sum_of_two(x, y):
    print x + y


sum_of_two(1, 2)
