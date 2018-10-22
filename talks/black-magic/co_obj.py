def a(b, c, d=1):
    pass

print(a.__code__)

print(a.__code__.co_varnames)

print(a.__defaults__)
