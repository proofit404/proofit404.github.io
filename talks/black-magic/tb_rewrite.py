import sys
from types import CodeType


def make_tb():

    exc_type, exc_value, tb = sys.exc_info()
    filename = 'xxx.html'
    location = 'html'
    gbs = {'exc_value': exc_type()}
    code = compile('\n' * (tb.tb_lineno - 1) + 'raise exc_value', filename, 'exec')
    code = CodeType(0, code.co_kwonlyargcount, code.co_nlocals, code.co_stacksize, code.co_flags, code.co_code, code.co_consts, code.co_names, code.co_varnames, filename, location, code.co_firstlineno, code.co_lnotab, (), ())
    try:
        exec(code, gbs)
    except:
        exc_info = sys.exc_info()
        new_tb = exc_info[2].tb_next
    return new_tb


try:
    hello
except Exception as e:
    tb = make_tb()
    raise e.with_traceback(tb)
