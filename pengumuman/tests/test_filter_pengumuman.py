from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from pengumuman.models import MataKuliah, JenisPengumuman, Ruang, \
    Sesi, StatusPengumuman, Pengumuman
from pengumuman.views import filter_pengumuman

User = get_user_model()


class FilterPengumumanTest(TestCase):
    def setUp(self):
        tanggal_kelas = "2016-11-16T07:00:18.130822+00:00"
        mata_kuliah = MataKuliah.objects.create(nama="Alin")
        jenis_pengumuman = JenisPengumuman.objects.create(nama="Asistensi")
        ruang = Ruang.objects.create(nama="3111")
        sesi = Sesi.objects.create(nama="16.00 - 17.40")
        status_pengumuman = StatusPengumuman.objects.create(nama="Ditunda")
        user = User.objects.create(username='julia.ningrum', password='admin', is_admin=True)
        User.objects.create(username='yusuf.tri',
                            password='mahasiswa')
        Pengumuman.objects.create(tanggal_kelas=tanggal_kelas, pembuat=user,
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
        response = client.get('/api/pengumuman/filter-pengumuman?tanggal=16-11-2016')

        self.assertEqual(response.status_code, 401)

    def test_request_not_admin(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='yusuf.tri')
        view = filter_pengumuman

        # Make an authenticated request to the view...
        request = factory.get('/api/pengumuman/filter-pengumuman?tanggal=16-11-2016')
        force_authenticate(request, user=user)
        response = view(request)
        data_date = list(response.data["pengumuman_response"])
        self.assertEqual(len(data_date), 1)


    def test_request_as_admin(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='julia.ningrum')
        view = filter_pengumuman

        # Make an authenticated request to the view...
        request = factory.get('/api/pengumuman/filter-pengumuman?tanggal=16-11-2016')
        force_authenticate(request, user=user)
        response = view(request)
        data_date = list(response.data["pengumuman_response"])
        self.assertEqual(len(data_date), 2)

    def test_invalid_date_format(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='julia.ningrum')
        view = filter_pengumuman

        # Make an authenticated request to the view...
        request = factory.get('/api/pengumuman/filter-pengumuman?tanggal=az-11-2016')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 400)
