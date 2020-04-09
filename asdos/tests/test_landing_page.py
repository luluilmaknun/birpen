from django.apps import apps
from django.test import TestCase
from rest_framework.test import APIClient

from asdos.apps import AsdosConfig


class LandingPageConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(AsdosConfig.name, 'asdos')
        self.assertEqual(apps.get_app_config('asdos').name, 'asdos')


class LandingPageApiTest(TestCase):
    def test_get_page(self):
        client = APIClient()
        response = client.get('/api/asdos/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.data['result']['message'], "asdos placeholder message")
