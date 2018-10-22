import sys


def x(): pass


_srcfile = x.__code__.co_filename


def get_caller():
    f = sys._getframe()
    f = f.f_back
    while hasattr(f, 'f_code'):
        co = f.f_code
        filename = co.co_filename
        if filename == _srcfile:
            f = f.f_back
            continue
        print(co.co_name)
        return
