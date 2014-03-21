import requests

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
        res = requests.get(self.address)
        status = res.status_code == 200
        hc = HealthCheck(url=self, status_code=res.status_code, status=status)
        hc.save()


class HealthCheck(models.Model):
    '''A status of a checking url proccess.
    '''

    url = models.ForeignKey('Url')
    status = models.BooleanField()
    status_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

