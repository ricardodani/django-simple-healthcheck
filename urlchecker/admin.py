from django.contrib import admin

from .models import Url

class UrlAdmin(admin.ModelAdmin):
    pass

admin.site.register(Url, UrlAdmin)
