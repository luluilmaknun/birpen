
from django.db import IntegrityError
from django.test import TestCase

from pengumuman.models import MataKuliah, JenisPengumuman, Ruang, \
    Sesi, StatusPengumuman, Pengumuman, User


class PengumumanModelTest(TestCase):
    def test_model_can_create(self):
        tanggal_kelas = "2016-11-16T22:31:18.130822+00:00"
        mata_kuliah = MataKuliah.objects.create(nama="Alin")
        jenis_pengumuman = JenisPengumuman.objects.create(nama="Asistensi")
        ruang = Ruang.objects.create(nama="3111")
        sesi = Sesi.objects.create(nama="16.00 - 17.40")
        status_pengumuman = StatusPengumuman.objects.create(nama="Ditunda")
        user = User.objects.create(username='julia.ningrum',
                                   password='admin', is_admin=True)

        Pengumuman.objects.create(tanggal_kelas=tanggal_kelas, pembuat=user,
                                  nama_mata_kuliah=mata_kuliah, jenis_pengumuman=jenis_pengumuman,
                                  nama_dosen="Dosen S.kom", nama_asisten="Asistenku",
                                  nama_ruang=ruang, nama_sesi=sesi,
                                  nama_status_pengumuman=status_pengumuman, komentar="")

        count = Pengumuman.objects.all().count()
        self.assertEqual(count, 1)

    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            Pengumuman.objects.create(pembuat=None)

    def test_soft_delete(self):
        tanggal_kelas = "2016-11-16T22:31:18.130822+00:00"
        mata_kuliah = MataKuliah.objects.create(nama="Alin")
        jenis_pengumuman = JenisPengumuman.objects.create(nama="Asistensi")
        ruang = Ruang.objects.create(nama="3111")
        sesi = Sesi.objects.create(nama="16.00 - 17.40")
        status_pengumuman = StatusPengumuman.objects.create(nama="Ditunda")
        user = User.objects.create(username='julia.ningrum',
                                   password='admin', is_admin=True)

        Pengumuman.objects.create(tanggal_kelas=tanggal_kelas, pembuat=user,
                                  nama_mata_kuliah=mata_kuliah, jenis_pengumuman=jenis_pengumuman,
                                  nama_dosen="Dosen S.kom", nama_asisten="Asistenku",
                                  nama_ruang=ruang, nama_sesi=sesi,
                                  nama_status_pengumuman=status_pengumuman, komentar="")
        count = Pengumuman.objects.all().count()
        self.assertEqual(count, 1)

        Pengumuman.objects.all().delete()
        count_without_soft_deleted = Pengumuman.objects.all().count()
        count_with_soft_deleted = Pengumuman.all_objects.all().count()
        self.assertEqual(count_without_soft_deleted, 0)
        self.assertEqual(count_with_soft_deleted, 1)
