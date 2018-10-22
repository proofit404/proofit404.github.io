import rq

import lib

with rq.Connection():
    q = rq.Queue('default')
    q.enqueue(lib.add, 1, 2)
