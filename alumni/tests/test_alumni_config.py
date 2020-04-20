from django.apps import apps
from django.test import TestCase

from alumni.apps import AlumniConfig


class AlumniConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(AlumniConfig.name, 'alumni')
        self.assertEqual(apps.get_app_config('alumni').name, 'alumni')
