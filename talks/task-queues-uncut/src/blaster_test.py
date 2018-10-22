import rb

cluster = rb.Cluster(
    hosts={
        0: {'port': 6379},
        1: {'port': 6380},
        # 2: {'port': 6381},
    },
    host_defaults={
        'host': 'localhost',
    })

if raw_input('Flush? [y/N]').lower() == 'y':
    with cluster.all() as client:
        client.flushdb()

if raw_input('Write? [y/N]').lower() == 'y':
    with cluster.map() as client:
        for key, value in [
                ('foo', 1),
                ('bar', 2),
                ('baz', 3),
        ]:
            client.set(key, value)

stop = False
while not stop:
    results = {}
    with cluster.map() as client:
        for key in ['foo', 'bar', 'baz']:
            results[key] = client.get(key)
    for key, promise in results.iteritems():
        print '%s: %s' % (key, promise.value)
    stop = raw_input('Stop? [y/N]').lower() == 'y'
