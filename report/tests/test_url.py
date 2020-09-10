from django.urls import reverse, resolve
from django.http import  HttpRequest
from report.views import index
from django.test import TestCase

class TestUrls(TestCase):

    def test_index_url_is_resolve(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
