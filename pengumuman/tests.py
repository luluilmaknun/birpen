from django.apps import apps
from django.test import TestCase
from django.db import IntegrityError

from rest_framework.test import APIClient
from pengumuman.apps import PengumumanConfig
from .models import MataKuliah, JenisPengumuman, Ruang, Sesi, StatusPengumuman, Pengumuman


class LandingPageConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(PengumumanConfig.name, 'pengumuman')
        self.assertEqual(apps.get_app_config('pengumuman').name, 'pengumuman')


class LandingPageApiTest(TestCase):
    def test_get_pengumuman(self):
        client = APIClient()
        response = client.get('/api/pengumuman/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.data['result']['message'], "pengumuman placeholder message")


class MataKuliahModelTest(TestCase):
    def test_model_can_create(self):
        MataKuliah.objects.create(nama='PPL')

        count = MataKuliah.objects.all().count()
        self.assertEqual(count, 1)


    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            MataKuliah.objects.create(nama=None)


    def test_soft_delete(self):
        MataKuliah.objects.create(nama='PPL')
        count = MataKuliah.objects.all().count()
        self.assertEqual(count, 1)

        MataKuliah.objects.all().delete()
        count_without_soft_deleted = MataKuliah.objects.all().count()
        count_with_soft_deleted = MataKuliah.all_objects.all().count()
        self.assertEqual(count_without_soft_deleted, 0)
        self.assertEqual(count_with_soft_deleted, 1)


class JenisPengumumanModelTest(TestCase):
    def test_model_can_create(self):
        JenisPengumuman.objects.create(nama='Asistensi')

        count = JenisPengumuman.objects.all().count()
        self.assertEqual(count, 1)


    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            JenisPengumuman.objects.create(nama=None)


    def test_soft_delete(self):
        JenisPengumuman.objects.create(nama='PPL')
        count = JenisPengumuman.objects.all().count()
        self.assertEqual(count, 1)

        JenisPengumuman.objects.all().delete()
        count_without_soft_deleted = JenisPengumuman.objects.all().count()
        count_with_soft_deleted = JenisPengumuman.all_objects.all().count()
        self.assertEqual(count_without_soft_deleted, 0)
        self.assertEqual(count_with_soft_deleted, 1)


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


class StatusPengumumanModelTest(TestCase):
    def test_model_can_create(self):
        StatusPengumuman.objects.create(nama='Asistensi')

        count = StatusPengumuman.objects.all().count()
        self.assertEqual(count, 1)


    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            StatusPengumuman.objects.create(nama=None)


    def test_soft_delete(self):
        StatusPengumuman.objects.create(nama='PPL')
        count = StatusPengumuman.objects.all().count()
        self.assertEqual(count, 1)

        StatusPengumuman.objects.all().delete()
        count_without_soft_deleted = StatusPengumuman.objects.all().count()
        count_with_soft_deleted = StatusPengumuman.all_objects.all().count()
        self.assertEqual(count_without_soft_deleted, 0)
        self.assertEqual(count_with_soft_deleted, 1)


class PengumumanModelTest(TestCase):
    def test_model_can_create(self):
        tanggal_kelas = "2016-11-16T22:31:18.130822+00:00"
        mata_kuliah = MataKuliah.objects.create(nama="Alin")
        jenis_pengumuman = JenisPengumuman.objects.create(nama="Asistensi")
        ruang = Ruang.objects.create(nama="3111")
        sesi = Sesi.objects.create(nama="16.00 - 17.40")
        status_pengumuman = StatusPengumuman.objects.create(nama="Ditunda")

        Pengumuman.objects.create(tanggal_kelas=tanggal_kelas, nama_pembuat="Jaraka", \
            nama_mata_kuliah=mata_kuliah, jenis_pengumuman=jenis_pengumuman, \
            nama_dosen="Dosen S.kom", nama_asisten="Asistenku", nama_ruang=ruang, \
            nama_sesi=sesi, nama_status_pengumuman=status_pengumuman, komentar="")

        count = Pengumuman.objects.all().count()
        self.assertEqual(count, 1)


    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            Pengumuman.objects.create(nama_pembuat=None)


    def test_soft_delete(self):
        tanggal_kelas = "2016-11-16T22:31:18.130822+00:00"
        mata_kuliah = MataKuliah.objects.create(nama="Alin")
        jenis_pengumuman = JenisPengumuman.objects.create(nama="Asistensi")
        ruang = Ruang.objects.create(nama="3111")
        sesi = Sesi.objects.create(nama="16.00 - 17.40")
        status_pengumuman = StatusPengumuman.objects.create(nama="Ditunda")

        Pengumuman.objects.create(tanggal_kelas=tanggal_kelas, nama_pembuat="Jaraka", \
            nama_mata_kuliah=mata_kuliah, jenis_pengumuman=jenis_pengumuman, \
            nama_dosen="Dosen S.kom", nama_asisten="Asistenku", nama_ruang=ruang, \
            nama_sesi=sesi, nama_status_pengumuman=status_pengumuman, komentar="")
        count = Pengumuman.objects.all().count()
        self.assertEqual(count, 1)

        Pengumuman.objects.all().delete()
        count_without_soft_deleted = Pengumuman.objects.all().count()
        count_with_soft_deleted = Pengumuman.all_objects.all().count()
        self.assertEqual(count_without_soft_deleted, 0)
        self.assertEqual(count_with_soft_deleted, 1)
