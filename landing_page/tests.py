from django.apps import apps
from django.test import TestCase
from landing_page.apps import LandingPageConfig


class LandingPageConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(LandingPageConfig.name, 'landing_page')
        self.assertEqual(apps.get_app_config('landing_page').name, 'landing_page')
