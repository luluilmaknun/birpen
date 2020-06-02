from django.apps import apps
from django.test import TestCase

from karya_akhir.apps import KaryaAkhirConfig


class KaryaAkhirConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(KaryaAkhirConfig.name, 'karya_akhir')
        self.assertEqual(apps.get_app_config('karya_akhir').name, 'karya_akhir')
