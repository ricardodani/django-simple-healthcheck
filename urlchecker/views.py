from django.views.generic import TemplateView
from django.shortcuts import render


class HealthCheckListUrlsView(TemplateView):

    template_name = 'urlchecker/list-urls.html'
