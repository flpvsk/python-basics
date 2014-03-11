def unique(l):
    return list(set(l))

print(unique([1, 1, 11, 2, 2, 3, 3, 4, 5]))
print(range(5)*2)
print(unique(range(5)*2))

def divide(a, b):
    try:
        return True, float(a) / b
    except (ZeroDivisionError, TypeError):
        return False, None

print(divide(4, 5))
print(divide(4, False))
print(divide(4, None))
print(divide(4, 2))
