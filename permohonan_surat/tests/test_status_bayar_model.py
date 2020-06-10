from django.test import TestCase
from django.db import IntegrityError

from permohonan_surat.models import StatusBayar


class StatusBayarTest(TestCase):
    def test_model_can_create(self):
        initial_count = StatusBayar.objects.all().count()

        StatusBayar.objects.create(nama='Lunas')

        count = StatusBayar.objects.all().count()
        self.assertEqual(count, initial_count + 1)

    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            StatusBayar.objects.create(nama=None)
