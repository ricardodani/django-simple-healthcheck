from django.conf.urls import patterns, url

from .views import HealthCheckListUrlsView, HealthCheckDetailUrlView

urlpatterns = patterns('',
    url(r'^$', HealthCheckListUrlsView.as_view(), name='healthcheck_list_urls'),
    url(r'^(?P<pk>\d+)/$', HealthCheckDetailUrlView.as_view(), name='healthcheck_detail_url'),
)
