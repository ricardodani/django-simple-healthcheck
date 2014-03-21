from django.test import TestCase, Client
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
        self.client = Client()

    def test_healthcheck_view_returns_200(self):
        r = self.client.get('/healthcheck/')
        self.assertEquals(r.status_code, 200)

