from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from permohonan_surat.models import Pesanan
from permohonan_surat.models import StatusBayar

User = get_user_model()


class PesananTest(TestCase):
    def setUp(self):
        self.status_bayar = StatusBayar.objects.create(nama='Lunas')
        self.user = User.objects.create(username="muhammad.yusuf", password="yusuf")

    def test_model_can_create(self):
        initial_count = Pesanan.objects.all().count()

        Pesanan.objects.create(pemesan=self.user,
                               nama_pemesan='Lunas',
                               npm_pemesan='1706978821',
                               status_bayar=self.status_bayar)

        count = Pesanan.objects.all().count()
        self.assertEqual(count, initial_count + 1)

    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            Pesanan.objects.create(status_bayar=None)
