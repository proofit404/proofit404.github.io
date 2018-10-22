import pdb


def foo():
    pdb.set_trace()
    yield from bar()
    yield from bar()


def bar():
    yield 1


a = foo()
print(next(a))
print(next(a))
