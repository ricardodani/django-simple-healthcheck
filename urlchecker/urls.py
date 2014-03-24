from django.conf import settings
from django.conf.urls import patterns, url

from .views import ListUrlsView, DetailUrlView

urlpatterns = patterns('',
    url(r'^$', ListUrlsView.as_view(),
        name='healthcheck_list_urls'),
    url(r'^(?P<pk>\d+)/$', DetailUrlView.as_view(),
        name='healthcheck_detail_url'),
)

if settings.DEBUG or True:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve'),
    )
