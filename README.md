django-simple-healthcheck
=========================

A simple URL healthcheck

Instructions
------------

Install requirements:
      
        pip install -r requirements.txt

Prepare database::

        ./manage.py syncdb --migrate


To run the check_urls command
--------------------------

Normal proccess:

      ./manage.py check_urls

As a daemon:

      ./manage.py check_urls --daemon


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
