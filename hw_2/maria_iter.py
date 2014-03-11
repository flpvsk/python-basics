def unique(lst):
    seen = set()
    return [el for el in lst if el not in seen and not seen.add(el)]
 
lst = [1, 2, 1, 3, 4, 3, 3, 3]
print("Initial list: {}".format(lst))
print("List with unique elements: {}".format(unique(lst)))