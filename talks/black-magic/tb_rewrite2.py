import sys
from types import CodeType


def make_tb():

    exc_type, exc_value, tb = sys.exc_info()
    filename = 'xxx.html'
    location = 'html'
    gbs = {'exc_value': exc_type()}
    code = compile('\n' * 21 + 'raise exc_value', filename, 'exec')
    code = CodeType(0, code.co_kwonlyargcount, code.co_nlocals, code.co_stacksize, code.co_flags, code.co_code, code.co_consts, code.co_names, code.co_varnames, filename, location, code.co_firstlineno, code.co_lnotab, (), ())
    try:
        exec(code, gbs)
    except:
        exc_info = sys.exc_info()
        new_tb = exc_info[2].tb_next
    return new_tb


def trim(exc):

    f = exc.__traceback__.tb_frame
    set_f_back(f.f_back.f_back, f)


def init_ugly_crap():

    import ctypes

    class _PyObject(ctypes.Structure):
        pass
    _PyObject._fields_ = [
        ('ob_refcnt', ctypes.c_ssize_t),
        ('ob_type', ctypes.POINTER(_PyObject)),
    ]

    class _PyCodeObject(ctypes.Structure):
        _fields_ = [
            ('co_argcount', ctypes.c_int),
            ('co_kwonlyargcount', ctypes.c_int),
            ('co_nlocals', ctypes.c_int),
            ('co_stacksize', ctypes.c_int),
            ('co_flags', ctypes.c_int),
            ('co_firstlineno', ctypes.c_int),
            ('co_code', ctypes.POINTER(_PyObject)),
            ('co_consts', ctypes.POINTER(_PyObject)),
            ('co_names', ctypes.POINTER(_PyObject)),
            ('co_varnames', ctypes.POINTER(_PyObject)),
            ('co_freevars', ctypes.POINTER(_PyObject)),
            ('co_cellvars', ctypes.POINTER(_PyObject)),
            ('co_cell2ar', ctypes.c_ubyte),
            ('co_filename', ctypes.POINTER(_PyObject)),
            ('co_name', ctypes.POINTER(_PyObject)),
            ('co_lnotab', ctypes.POINTER(_PyObject)),
            ('co_zombieframe', ctypes.c_void_p),
            ('co_weakreflist', ctypes.POINTER(_PyObject)),
            ('co_extra', ctypes.c_void_p),
        ]

    class _PyTryBlock(ctypes.Structure):
        _fields_ = [
            ("b_type", ctypes.c_int),
            ("b_handler", ctypes.c_int),
            ("b_level", ctypes.c_int),
        ]

    class _PyFrameObject(ctypes.Structure):
        pass
    _PyFrameObject._fields_ = [
        ('f_back', ctypes.POINTER(_PyFrameObject)),
        ('f_code', ctypes.POINTER(_PyCodeObject)),
        ('f_builtins', ctypes.POINTER(_PyObject)),
        ('f_globals', ctypes.POINTER(_PyObject)),
        ('f_locals', ctypes.POINTER(_PyObject)),
        ('f_valuestack', ctypes.POINTER(_PyObject)),

        ('f_stacktop', ctypes.POINTER(_PyObject)),
        ('f_trace', ctypes.POINTER(_PyObject)),

        ('f_exc_type', ctypes.POINTER(_PyObject)),
        ('f_exc_value', ctypes.POINTER(_PyObject)),
        ('f_exc_traceback', ctypes.POINTER(_PyObject)),

        ('f_gen', ctypes.POINTER(_PyObject)),

        ("f_lasti", ctypes.c_int),
        ("f_lineno", ctypes.c_int),
        ("f_iblock", ctypes.c_int),
        ("f_executing", ctypes.c_char),
        ('f_blockstack', ctypes.POINTER(_PyTryBlock)),
        ('f_localsplus', ctypes.POINTER(_PyObject)),
    ]

    def _set_f_back(upper, lower):
        _upper = _PyFrameObject.from_address(id(upper))
        _lower = _PyFrameObject.from_address(id(lower))
        _upper.f_back = ctypes.pointer(_lower)

    return _set_f_back


set_f_back = init_ugly_crap()


def test():

    try:
        hello
    except Exception as e:
        tb = make_tb()
        new_exc = e.with_traceback(tb)
        # trim(new_exc)
        raise new_exc


def test2(): test()

def test3(): test2()

def test4(): test3()

test4()
