from django.test import TestCase
from django.db import IntegrityError

from karya_akhir.models import ProgramStudi


class ProgramStudiTest(TestCase):
    def test_model_can_create(self):
        initial_count = ProgramStudi.objects.all().count()

        ProgramStudi.objects.create(nama='Akuntansi')

        count = ProgramStudi.objects.all().count()
        self.assertEqual(count, initial_count + 1)

    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            ProgramStudi.objects.create(nama=None)
