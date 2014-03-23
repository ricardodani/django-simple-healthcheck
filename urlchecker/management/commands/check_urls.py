# -*- coding: utf-8 -*-

import os
import daemon
import time
from multiprocessing import Process
from optparse import make_option

from django.core.management.base import BaseCommand

from urlchecker.models import Url


class Command(BaseCommand):

    @staticmethod
    def process_info():
        info = ''
        if hasattr(os, 'getppid'): # only avaible on unix
            info = '[ppid={}]'.format(os.getppid())
        info += '[pid={}]'.format(os.getpid())
        return info

    def check_url(self, url):
        if self.verbosity > 0:
            print 'Running urlchecker to {}. {}'.format(url, self.process_info())
        while True:
            if self.verbosity > 1:
                print u'Checking {} url. {}'.format(url, self.process_info())
            url.check_url()
            time.sleep(url.check_interval)

    def main_process(self):
        urls = Url.objects.all()
        for url in urls:
            p = Process(target=self.check_url, args=(url,))
            p.start()

    def handle(self, *args, **options):
        self.verbosity = int(options['verbosity'])
        p = Process(target=self.main_process)
        p.start()
        p.join()
