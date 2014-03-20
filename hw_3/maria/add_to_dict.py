def add_to_dict(dict, **kwargs):
    for key, value in kwargs.iteritems():
        dict[key] = value

d = {"x": 1}

print("Test 1 - without arguments")
add_to_dict(d)
print("Result: {}".format(d))

print("Test 2 - add 1 argument")       
add_to_dict(d, y = 5)
print("Result: {}".format(d))

print("Test 3 - add 5 arguments (total dict arg - 7)")       
add_to_dict(d, a = 5, b = 3, c = "test", d = "", e = 3.56)
print("Result: {}".format(d))