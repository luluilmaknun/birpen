from django.test import TestCase
from django.db import IntegrityError

from karya_akhir.models import JenisKaryaAkhir


class JenisKaryaAkhirTest(TestCase):
    def test_model_can_create(self):
        initial_count = JenisKaryaAkhir.objects.all().count()

        JenisKaryaAkhir.objects.create(nama='Skripsi')

        count = JenisKaryaAkhir.objects.all().count()
        self.assertEqual(count, initial_count + 1)

    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            JenisKaryaAkhir.objects.create(nama=None)
