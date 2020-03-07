from django.test import TestCase
from django.db import IntegrityError

from pengumuman.models import Ruang


class RuangModelTest(TestCase):
    def test_model_can_create(self):
        Ruang.objects.create(nama='3112')

        count = Ruang.objects.all().count()
        self.assertEqual(count, 1)

    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            Ruang.objects.create(nama=None)

    def test_soft_delete(self):
        Ruang.objects.create(nama='PPL')
        count = Ruang.objects.all().count()
        self.assertEqual(count, 1)

        Ruang.objects.all().delete()
        count_without_soft_deleted = Ruang.objects.all().count()
        count_with_soft_deleted = Ruang.all_objects.all().count()
        self.assertEqual(count_without_soft_deleted, 0)
        self.assertEqual(count_with_soft_deleted, 1)
