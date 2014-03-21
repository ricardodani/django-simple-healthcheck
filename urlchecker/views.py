from django.views.generic import TemplateView

from .models import Url


class HealthCheckListUrlsView(TemplateView):

    template_name = 'urlchecker/list-urls.html'

    def get_context_data(self, **kwargs):
        urls = Url.objects.all()
        context = dict(urls=urls)
        return context
