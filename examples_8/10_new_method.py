
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if Singleton._instance:
            return Singleton._instance
        Singleton._isntance = super(cls).__new__(cls, *args, **kwargs)
        return Singleton._instance


    def __init__(*args):
        print args


Singleton('x')
