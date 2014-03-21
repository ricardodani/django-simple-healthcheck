from django.views.generic import TemplateView, DetailView

from .models import Url, HealthCheck


class HealthCheckListUrlsView(TemplateView):

    template_name = 'urlchecker/url_list.html'

    def get_context_data(self, **kwargs):
        urls = Url.objects.all()
        context = dict(urls=urls)
        return context


class HealthCheckDetailUrlView(DetailView):

    model = Url
