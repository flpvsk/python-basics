import re

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


def wc(s):
    return {"symbols": len(re.findall(r'\w', s)),
            "words": len(re.findall(r'\w\w*', s)),
            "lines": s.count("\n") + 1}

s = """d   ss
                   ddd
123_45f
dd
d"""

print(wc(s))
print(re.findall(r'\w', s))