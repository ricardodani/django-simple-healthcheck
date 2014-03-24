from django.views.generic import TemplateView, DetailView

from .models import Url


class ListUrlsView(TemplateView):

    template_name = 'urlchecker/url_list.html'

    def get_context_data(self, **kwargs):
        urls = Url.objects.all()
        context = dict(urls=urls)
        return context


class DetailUrlView(DetailView):

    queryset = Url.objects.all().order_by('-created_at')
