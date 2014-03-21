# -*- coding: utf-8 -*-

import daemon
import time
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand

from urlchecker.models import Url


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option(
            '--daemon',
            action='store_true',
            dest='daemon',
            default=False,
            help='Set the command to run as a daemon'
        ),
    )

    @staticmethod
    def check_urls():
        urls = Url.objects.all()
        if urls:
            for url in urls:
                url.check_url()
                print u'Url {} cheked.'.format(url)
        else:
            print 'No Url to check.'

    def tasks_loop(self):
        while True:
            self.check_urls()
            time.sleep(settings.HEALTHCHECKER_PERIOD_IN_SECONDS)

    def handle(self, *args, **options):
        if options['daemon']:
            with daemon.DaemonContext():
                self.tasks_loop()
        else:
            self.tasks_loop()
