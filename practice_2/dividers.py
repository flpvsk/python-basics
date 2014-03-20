def dividers(x):
    return [j for j in range(1, x+1) if x % j == 0]

print(dividers(10))
print(dividers(11))
print(dividers(256))


def booleans(l):
    return [bool(x) for x in l]

print(booleans([1, 2, None, False]))
print(booleans([]))
print(booleans([1, 2, None, False, "kjfhgkarhgila"]))