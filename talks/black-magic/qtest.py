import q

@q
def foo(bar):
    """The best function ever..."""
    return bar + '!!!'


def write(text):
    pass


prefix = 'xxx'
sep = ' '

def test():
    write(prefix + q(sep or ''))
    write(q/prefix + (sep or ''))
    write(q|prefix + (sep or ''))

test()
foo(prefix)
