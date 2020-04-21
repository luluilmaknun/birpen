from django.apps import apps
from django.test import TestCase

from admin_birpen.apps import AdminBirpenConfig


class AdminBirpenConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(AdminBirpenConfig.name, 'admin_birpen')
        self.assertEqual(apps.get_app_config('admin_birpen').name, 'admin_birpen')
