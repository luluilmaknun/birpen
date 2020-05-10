from django.test import TestCase
from django.db import IntegrityError

from permohonan_surat.models import SuratTugasAkhir


class SuratTugasAkhirTest(TestCase):
    def test_model_can_create(self):
        initial_count = SuratTugasAkhir.objects.all().count()

        SuratTugasAkhir.objects.create(nama='Surat Keterangan Karya Akhir Siap Uji')

        count = SuratTugasAkhir.objects.all().count()
        self.assertEqual(count, initial_count + 1)

    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            SuratTugasAkhir.objects.create(nama=None)
