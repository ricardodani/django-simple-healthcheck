django-simple-healthcheck
=========================

A simple URL healthcheck django project.

Instructions
------------

Install requirements:

    pip install -r requirements.txt

Prepare database:

    ./manage.py syncdb --migrate

Settings
--------

Define the default sleep interval for an url check process:

    URLCHECKER_INTERVAL = 10 # 10 seconds

To run the check_urls command
--------------------------



    ./manage.py check_urls


Create some URL's
-----------------

Access /admin to create some Urls


Author
========

Ricardo Dani
github.com/ricardodani


License
========

GPL
