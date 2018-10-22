import sys
import linecache


def set_trace():
    sys.settrace(dispatch)


def dispatch(frame, event, arg):
    line = linecache.getline(
        frame.f_code.co_filename,
        frame.f_lineno,
    )
    print(line.strip())
    cmd = True
    while cmd:
        cmd = input('(Mydbg) ')
        run_command(cmd, frame)
    return dispatch


def run_command(cmd, frame):
    if cmd in frame.f_locals:
        print(frame.f_locals[cmd])
    if cmd in frame.f_globals:
        print(frame.f_globals[cmd])
