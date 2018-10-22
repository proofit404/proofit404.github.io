Example of hexagonal architecture approach for django applications.

Setup
-----

To run this app you need to do following steps::

    python3.5 -m venv .env
    . .env/bin/activate
    pip install -r requirements.txt
    export PYTHONPATH=$PWD
    export DJANGO_SETTINGS_MODULE=hexagon.settings
    django-admin migrate
    django-admin createsuperuser
    django-admin runserver

Usage
-----

Open Django Admin page and login in to our site

http://localhost:8000/admin/

Now you can subscribe to some interesting services

http://localhost:8000/

Layout
------

Quick guide for preferred source code navigation

1. Learn ``attrs`` library https://attrs.readthedocs.io
2. Learn ``dependencies`` library https://dependencies.readthedocs.io
3. ``hexagon`` package contains django project with settings and root
   url config.
4. ``web`` package contains site frontend written in django views.
5. ``business.usecases`` package contains business logic related to
   site functionality.
6. ``business.entities`` package contains business logic related to
   the domain model and high level object relationship.
7. ``db`` package contains persistence layer written in django models.

Key feature here that we don't use single django app for web frontend,
database operations and business logic.
