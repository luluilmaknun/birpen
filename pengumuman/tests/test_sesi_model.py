from django.test import TestCase
from django.db import IntegrityError

from pengumuman.models import Sesi


class SesiModelTest(TestCase):
    def test_model_can_create(self):
        Sesi.objects.create(nama='Asistensi')

        count = Sesi.objects.all().count()
        self.assertEqual(count, 1)

    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            Sesi.objects.create(nama=None)

    def test_soft_delete(self):
        Sesi.objects.create(nama='PPL')
        count = Sesi.objects.all().count()
        self.assertEqual(count, 1)

        Sesi.objects.all().delete()
        count_without_soft_deleted = Sesi.objects.all().count()
        count_with_soft_deleted = Sesi.all_objects.all().count()
        self.assertEqual(count_without_soft_deleted, 0)
        self.assertEqual(count_with_soft_deleted, 1)
