from django.apps import apps
from django.test import TestCase

from asdos.apps import AsdosConfig


class LandingPageConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(AsdosConfig.name, 'asdos')
        self.assertEqual(apps.get_app_config('asdos').name, 'asdos')
