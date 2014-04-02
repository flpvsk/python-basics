def add_to_dict(d, **kwargs):
    for x in kwargs:
        d[x] = kwargs[x]

d = {"a": "a"}
add_to_dict(d, b="b", c="c")
print d