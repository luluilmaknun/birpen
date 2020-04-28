from django.test import TestCase
from django.db import IntegrityError

from permohonan_surat.models import SuratAkademik
from permohonan_surat.models import Pesanan
from permohonan_surat.models import StatusSurat
from permohonan_surat.models import StatusBayar
from permohonan_surat.models import PesananSuratAkademik


class PesananSuratAkademikTest(TestCase):
    def setUp(self):
        self.surat_akademik = SuratAkademik.objects.create(jenis_dokumen="Transkrip nilai",
                                                           harga_mahasiswa=0, harga_alumni=10000)

        status_bayar = StatusBayar.objects.create(nama='Lunas')
        self.pesanan = Pesanan.objects.create(nama_pemesan='Lunas', npm_pemesan='1706978821',
                                              status_bayar=status_bayar)

        self.status_surat = StatusSurat.objects.create(nama='Menunggu Diproses')

    def test_model_can_create(self):
        initial_count = PesananSuratAkademik.objects.all().count()

        PesananSuratAkademik.objects.create(pesanan=self.pesanan,
                                            surat_akademik=self.surat_akademik,
                                            status_surat=self.status_surat,
                                            jumlah=1)

        count = PesananSuratAkademik.objects.all().count()
        self.assertEqual(count, initial_count + 1)

    def test_unique_combination_pesanan_and_surat_akademik(self):
        PesananSuratAkademik.objects.create(pesanan=self.pesanan,
                                            surat_akademik=self.surat_akademik,
                                            status_surat=self.status_surat,
                                            jumlah=1)

        with self.assertRaises(IntegrityError):
            PesananSuratAkademik.objects.create(pesanan=self.pesanan,
                                                surat_akademik=self.surat_akademik,
                                                status_surat=self.status_surat,
                                                jumlah=1)

    def test_model_not_create_without_pesanan(self):
        with self.assertRaises(IntegrityError):
            PesananSuratAkademik.objects.create(pesanan=None,
                                                surat_akademik=self.surat_akademik,
                                                status_surat=self.status_surat,
                                                jumlah=1)

    def test_model_not_create_without_surat_akademik(self):
        with self.assertRaises(IntegrityError):
            PesananSuratAkademik.objects.create(pesanan=self.pesanan,
                                                surat_akademik=None,
                                                status_surat=self.status_surat,
                                                jumlah=1)

    def test_model_not_create_without_status_surat(self):
        with self.assertRaises(IntegrityError):
            PesananSuratAkademik.objects.create(pesanan=self.pesanan,
                                                surat_akademik=self.surat_akademik,
                                                status_surat=None,
                                                jumlah=1)
