from django.test import TestCase
from django.db import IntegrityError

from permohonan_surat.models import StatusSurat


class StatusSuratTest(TestCase):
    def test_model_can_create(self):
        initial_count = StatusSurat.objects.all().count()

        StatusSurat.objects.create(nama='Menunggu tanda tangan dekan')

        count = StatusSurat.objects.all().count()
        self.assertEqual(count, initial_count + 1)

    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            StatusSurat.objects.create(nama=None)
