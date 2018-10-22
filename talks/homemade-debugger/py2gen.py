import pdb


def foo():
    pdb.set_trace()
    x = yield 1
    y = yield 2
    z = yield 3


a = foo()
print(next(a))
print(next(a))
print(next(a))
