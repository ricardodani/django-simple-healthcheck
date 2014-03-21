from django.db import models

class Url(models.Model):
    '''A Url to be checked.
    '''

    address = models.CharField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Status(models.Model):
    pass
