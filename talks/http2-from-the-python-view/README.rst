Generate certs
==============

.. code:: bash

    openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes


Running channels
================

.. code:: bash

    PYTHONPATH=$PWD DJANGO_SETTINGS_MODULE=channels_example.settings django-admin runworker
    PYTHONPATH=$PWD daphne -e ssl:port=8000:privateKey=key.pem:certKey=cert.pem channels_example.asgi:channel_layer

Open https://127.0.0.1:8000/

Running twisted
===============

.. code:: bash

    .
