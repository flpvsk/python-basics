def to_bool(lst):
    booled_list = []
    for el in lst:
        booled_list.append(bool(el))
    return booled_list

lst = [0, 1, '', None, "String", 0.0, 0.234]
print("Initial list: {0}".format(', '.join(str(e) for e in lst)))
print("Booled list: {}".format(', '.join(str(e) for e in to_bool(lst))))

