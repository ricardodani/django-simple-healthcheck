from django.db import models

class Url(models.Model):
    '''A Url to be checked.
    '''

    address = models.URLField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.address


class HealthCheck(models.Model):

    url = models.ForeignKey('Url')
    status_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

