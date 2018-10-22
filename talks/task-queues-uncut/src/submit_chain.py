from celery import chain

import app

c = chain(app.add.s(1, 2), app.add.s(3), app.mul.s(6))
c()
