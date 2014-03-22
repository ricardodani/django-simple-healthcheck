import requests
import time

from django.db import models

class Url(models.Model):
    '''A Url to be checked.
    '''

    address = models.URLField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.address

    def check_url(self):
        t1 = time.time()
        hc = HealthCheck(url=self)
        try:
            res = requests.get(self.address)
        except requests.exceptions.ConnectionError:
            hc.status = False
        else:
            hc.status_code = res.status_code
            hc.status = res.status_code == 200
        t2 = time.time()
        hc.time = t2 - t1
        hc.save()

    @property
    def last_check(self):
        return self.healthcheck_set.first()

    @property
    def count_status(self):
        # TODO: this code needs refactoring (i think I can calculate this
        # only in database)
        status_codes = self.healthcheck_set.values('status_code')
        ocurrences = {}
        for s in status_codes:
            if s['status_code'] is None:
                s['status_code'] = 'Server Down'
            if s['status_code'] in ocurrences:
                ocurrences[s['status_code']] += 1
            else:
                ocurrences[s['status_code']] = 1
        return [(x, ocurrences[x]) for x in ocurrences]

    @property
    def status_percent(self):
        qs = self.healthcheck_set
        ok_count = float(qs.filter(status=True).count())
        all_count = qs.all().count()
        ok_rate =  ok_count / all_count if all_count else None
        if ok_rate:
            percent = int(ok_rate * 100)
            return {'success': percent, 'warning': 100 - percent}
        else:
            return {'success': 0, 'warning': 0}

class HealthCheck(models.Model):
    '''A status of a checking url proccess.
    '''

    url = models.ForeignKey('Url')
    status = models.BooleanField()
    status_code = models.IntegerField(null=True)
    time = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

