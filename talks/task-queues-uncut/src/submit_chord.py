from celery import chord

import app

ch = chord([app.add.s(1, 2), app.add.s(3, 4), app.mul.s(5, 6)])
ch(app.mul.s(7))
