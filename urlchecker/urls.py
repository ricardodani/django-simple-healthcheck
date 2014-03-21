from django.conf.urls import patterns, url

from .views import HealthCheckListUrlsView

urlpatterns = patterns('',
    url(r'^$', HealthCheckListUrlsView.as_view(), name='healthcheck_list_urls'),
)
