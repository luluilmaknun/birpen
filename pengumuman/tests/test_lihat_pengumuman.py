from datetime import datetime, timedelta

from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate

from pengumuman.models import MataKuliah, JenisPengumuman, Ruang, Sesi, StatusPengumuman, User, Pengumuman
from pengumuman.views import get_pengumuman_default


class LihatPengumumanTest(TestCase):
    def setUp(self):
        tanggal_kelas = datetime.now()
        mata_kuliah = MataKuliah.objects.create(nama="Alin")
        jenis_pengumuman = JenisPengumuman.objects.create(nama="Asistensi")
        ruang = Ruang.objects.create(nama="3111")
        sesi = Sesi.objects.create(nama="16.00 - 17.40")
        status_pengumuman = StatusPengumuman.objects.create(nama="Ditunda")
        user = User.objects.create(username='julia.ningrum', name='julia ningrum',
                                   npm='1204893059', password='admin', user_type=User.ADMIN)
        User.objects.create(username='yusuf.tri',
                            name='yusuf tri a.', npm='1701837382',
                            password='mahasiswa', user_type=User.MAHASISWA)
        Pengumuman.objects.create(tanggal_kelas=tanggal_kelas, pembuat=user,
                                  nama_mata_kuliah=mata_kuliah, jenis_pengumuman=jenis_pengumuman,
                                  nama_dosen="Dosen S.kom", nama_asisten="Asistennya",
                                  nama_ruang=ruang, nama_sesi=sesi,
                                  nama_status_pengumuman=status_pengumuman, komentar="")

        Pengumuman.objects.create(tanggal_kelas=tanggal_kelas + timedelta(days=1), pembuat=user,
                                  nama_mata_kuliah=mata_kuliah, jenis_pengumuman=jenis_pengumuman,
                                  nama_dosen="Dosen S.kom", nama_asisten="Asistennya",
                                  nama_ruang=ruang, nama_sesi=sesi,
                                  nama_status_pengumuman=status_pengumuman, komentar="")

        Pengumuman.objects.create(tanggal_kelas=tanggal_kelas, pembuat=user,
                                  nama_mata_kuliah=mata_kuliah, jenis_pengumuman=jenis_pengumuman,
                                  nama_dosen="Dosen S.kom", nama_asisten="Asistenku",
                                  nama_ruang=ruang, nama_sesi=sesi,
                                  nama_status_pengumuman=status_pengumuman, komentar="")
        Pengumuman.objects.filter(nama_asisten="Asistenku").delete()

    def test_request_without_authentication(self):
        client = APIClient()
        response = client.get('/api/pengumuman/get-pengumuman')

        self.assertEqual(response.status_code, 401)

    def test_request_not_admin(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='yusuf.tri')
        view = get_pengumuman_default

        # Make an authenticated request to the view...
        request = factory.get('/api/pengumuman/get-pengumuman')
        force_authenticate(request, user=user)
        response = view(request)
        data_today = list(response.data["pengumuman_today"])
        self.assertEqual(len(data_today), 1)
        data_tomo = list(response.data["pengumuman_tomo"])
        self.assertEqual(len(data_tomo), 1)

    def test_request_as_admin(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='julia.ningrum')
        view = get_pengumuman_default

        # Make an authenticated request to the view...
        request = factory.get('/api/pengumuman/get-pengumuman')
        force_authenticate(request, user=user)
        response = view(request)
        data_today = list(response.data["pengumuman_today"])
        self.assertEqual(len(data_today), 2)
        data_tomo = list(response.data["pengumuman_tomo"])
        self.assertEqual(len(data_tomo), 1)
