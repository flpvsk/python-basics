from examples_2.utils import print_stars

emtpy_dict = {}
non_empty_dict = {'key1': 'value1', 'key2': 'value2'}

# Dict element access
print("non_empty_dict['key1']  = %r" % non_empty_dict['key1'])
print("non_empty_dict.keys()   = %r" % non_empty_dict.keys())
print("non_empty_dict.values() = %r" % non_empty_dict.values())
print("non_emtpy_dict.items()  = %r" % non_empty_dict.items())
print_stars()

# Dicts are mutable
d = non_empty_dict.copy()
print("Before:                         %r" % d)
d['key1'] = 'new value1'
print("After d['key1'] = 'new value1': %r" % d)
del d['key1']
print("After del d['key1']:            %r" % d)
print_stars()

# Dicts are iterable (by key)
d = non_empty_dict.copy()
for key in d:
    print("In Loop. Key: %r, Value: %r" % (key, d[key]))
print_stars()

# Test if key is in dict
del d['key1']
print("'key1' in d: %r" % ('key1' in d))
print("'key2' in d: %r" % ('key2' in d))

#defualtdict
d=defaultdict(list)
d[1]
