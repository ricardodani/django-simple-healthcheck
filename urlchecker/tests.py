from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

from .models import Url


class UrlCheckerModelTestCase(TestCase):

    def test_url_address_cant_be_blank(self):
        url = Url()
        with self.assertRaises(ValidationError):
            url.clean_fields()

    def test_unicode_url(self):
        url = Url(address="/")
        self.assertEquals(url.address, url.__unicode__())


class UrlCheckerViewsTestCase(TestCase):

    def setUp(self):
        self.url = Url.objects.create(address="http://localhost/")
        self.client = Client()

    def test_view_list_urls_returns_200(self):
        r = self.client.get(reverse('healthcheck_list_urls'))
        self.assertEquals(r.status_code, 200)

    def test_view_detail_url_returns_200(self):
        r = self.client.get(reverse('healthcheck_detail_url',
                                    args=[self.url.id]))
        self.assertEquals(r.status_code, 200)
