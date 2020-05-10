from django.contrib.auth import get_user_model
from django.test import TestCase
from django.db import IntegrityError

from permohonan_surat.models import DataKaryaAkhir, JenisKaryaAkhir

User = get_user_model()

class DataKaryaAkhirTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="muhammad.yusuf", password="yusuf")
        self.jenis_karya_akhir = JenisKaryaAkhir.objects.create(nama="Skripsi")

    def test_model_can_create(self):
        initial_count = DataKaryaAkhir.objects.all().count()

        DataKaryaAkhir.objects.create(
            mahasiswa=self.user,
            peminatan_mahasiswa="Akuntansi Islam",
            jenis_karya_akhir=self.jenis_karya_akhir,
            sks_diperoleh=144,
            pembimbing="Ahmad Fauzan S.Ak",
            pembimbing_pendamping="Yusuf Tri S.Ak",
            judul_karya_id="Sebuah Karya",
            judul_karya_en="A Masterpiece"
        )

        count = DataKaryaAkhir.objects.all().count()
        self.assertEqual(count, initial_count + 1)

    def test_model_not_create_without_peminatan(self):
        with self.assertRaises(IntegrityError):
            DataKaryaAkhir.objects.create(
                mahasiswa=self.user,
                peminatan_mahasiswa=None,
                jenis_karya_akhir=self.jenis_karya_akhir,
                sks_diperoleh=144,
                pembimbing="Ahmad Fauzan S.Ak",
                pembimbing_pendamping="Yusuf Tri S.Ak",
                judul_karya_id="Sebuah Karya",
                judul_karya_en="A Masterpiece"
            )

    def test_model_not_create_without_sks_diperoleh(self):
        with self.assertRaises(IntegrityError):
            DataKaryaAkhir.objects.create(
                mahasiswa=self.user,
                peminatan_mahasiswa="Akuntansi Islam",
                jenis_karya_akhir=self.jenis_karya_akhir,
                sks_diperoleh=None,
                pembimbing="Ahmad Fauzan S.Ak",
                pembimbing_pendamping="Yusuf Tri S.Ak",
                judul_karya_id="Sebuah Karya",
                judul_karya_en="A Masterpiece"
            )

    def test_model_not_create_without_pembimbing(self):
        with self.assertRaises(IntegrityError):
            DataKaryaAkhir.objects.create(
                mahasiswa=self.user,
                peminatan_mahasiswa="Akuntansi Islam",
                jenis_karya_akhir=self.jenis_karya_akhir,
                sks_diperoleh=144,
                pembimbing=None,
                pembimbing_pendamping="Yusuf Tri S.Ak",
                judul_karya_id="Sebuah Karya",
                judul_karya_en="A Masterpiece"
            )

    def test_model_not_create_without_judul_karya_id(self):
        with self.assertRaises(IntegrityError):
            DataKaryaAkhir.objects.create(
                mahasiswa=self.user,
                peminatan_mahasiswa=None,
                jenis_karya_akhir=self.jenis_karya_akhir,
                sks_diperoleh=144,
                pembimbing="Ahmad Fauzan S.Ak",
                pembimbing_pendamping="Yusuf Tri S.Ak",
                judul_karya_id=None,
                judul_karya_en="A Masterpiece"
            )
