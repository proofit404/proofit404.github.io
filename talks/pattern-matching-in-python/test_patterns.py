from patterns import match, _, x, l


# Simple test.


@match(1)
def test(x):
    return 'one'


@match(2)
def test(x):
    return 'two'


assert test(1) == 'one'
assert test(2) == 'two'


# Greater test.


@match(x > 5)
def greater_test(x):
    return '{} greater then five'.format(x)


@match(_)
def greater_test(x):
    return '{} less then or equal to five'.format(x)


assert greater_test(7) == '7 greater then five'
assert greater_test(1) == '1 less then or equal to five'


# List test.


@match(_, _, [])
def foldr(f, initial, seq):
    return initial


@match(_, _, l[0], l[1:])
def foldr(f, initial, head, tail):
    return f(head, foldr(f, initial, tail))


assert foldr(lambda x, y: x + y, 0, [1, 2, 3, 4, 5]) == 15
assert foldr(lambda x, y: x * y, 1, [1, 2, 3, 4, 5]) == 120
