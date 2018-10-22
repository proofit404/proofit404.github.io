import os

from celery import Celery

app = Celery(__name__)

if os.getenv('USE_RABBITMQ'):
    app.conf.update(
        BROKER_URL='amqp://pyconru:pyconru@localhost:5672/pyconru',
        CELERY_RESULT_BACKEND='redis://localhost:6379/0')
elif os.getenv('USE_REDIS'):
    app.conf.update(
        BROKER_URL='redis://localhost:6380/0',
        CELERY_RESULT_BACKEND='redis://localhost:6381/0')
else:
    raise Exception('Bad')

for s in ['json', 'pickle', 'msgpack', 'yaml']:
    if os.getenv('USE_' + s.upper()):
        serializer = s
        break
else:
    serializer = 'json'

app.conf.update(
    CELERY_ACCEPT_CONTENT=[serializer],
    CELERY_TASK_SERIALIZER=serializer,
    CELERY_RESULT_SERIALIZER=serializer)

if os.getenv('USE_ACK'):
    app.conf['CELERY_ACKS_LATE'] = True

app.conf['CELERY_ROUTES'] = {
    'app.mul': {'queue': 'celery2'},
}


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x + y
