from django.apps import apps
from django.test import TestCase
from rest_framework.test import APIClient
from permohonan_surat.apps import PermohonanSuratConfig


class LandingPageConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(PermohonanSuratConfig.name, 'permohonan_surat')
        self.assertEqual(apps.get_app_config('permohonan_surat').name, 'permohonan_surat')


class LandingPageApiTest(TestCase):
    def test_get_pengumuman(self):
        client = APIClient()
        response = client.get('/api/permohonan-surat/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.data['result']['message'], "permohonan surat placeholder message")
