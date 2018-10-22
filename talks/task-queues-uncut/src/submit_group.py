from celery import group

import app

g = group(app.add.s(1, 2), app.mul.s(3, 4))
g()
