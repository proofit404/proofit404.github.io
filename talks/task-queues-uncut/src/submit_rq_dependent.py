import rq

import lib

with rq.Connection():
    q = rq.Queue('default')
    job = q.enqueue(lib.add, 1, 2)
    delayed = q.enqueue(lib.add, 1, 2, depends_on=job)
