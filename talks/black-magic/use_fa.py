from frame_access import get_caller


def x():

    print('before')
    get_caller()
    print('after')


def y():

    print('before')
    get_caller()
    print('after')


if __name__ == '__main__':
    x()
    y()
    get_caller()
