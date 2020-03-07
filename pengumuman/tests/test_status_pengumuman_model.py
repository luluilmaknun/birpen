from django.test import TestCase
from django.db import IntegrityError

from pengumuman.models import StatusPengumuman


class StatusPengumumanModelTest(TestCase):
    def test_model_can_create(self):
        StatusPengumuman.objects.create(nama='Asistensi')

        count = StatusPengumuman.objects.all().count()
        self.assertEqual(count, 1)

    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            StatusPengumuman.objects.create(nama=None)

    def test_soft_delete(self):
        StatusPengumuman.objects.create(nama='PPL')
        count = StatusPengumuman.objects.all().count()
        self.assertEqual(count, 1)

        StatusPengumuman.objects.all().delete()
        count_without_soft_deleted = StatusPengumuman.objects.all().count()
        count_with_soft_deleted = StatusPengumuman.all_objects.all().count()
        self.assertEqual(count_without_soft_deleted, 0)
        self.assertEqual(count_with_soft_deleted, 1)
