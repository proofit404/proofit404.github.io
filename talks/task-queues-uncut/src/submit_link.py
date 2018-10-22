import app

app.add.apply_async((1, 2), link=app.mul.s(3))
