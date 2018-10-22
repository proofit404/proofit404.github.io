class CtxMngr:

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_value, tb):

        return True


def x():

    with CtxMngr():
        1/0

    assert False, "we are here"


x()
