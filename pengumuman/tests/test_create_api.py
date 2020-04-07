from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode

from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from pengumuman.models import MataKuliah, JenisPengumuman, Ruang, \
    Sesi, StatusPengumuman, Pengumuman

from sso_ui.models import Admin

User = get_user_model()


class CreateApiTest(TestCase):
    def setUp(self):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        self.client = APIClient()

        user_1 = User.objects.create(username='athallah.annafis', password='mahasiswa')
        self.token_1 = jwt_encode_handler(jwt_payload_handler(user_1))

        user_2 = User.objects.create(username='julia.ningrum', password='admin')
        Admin.objects.create(username=user_2.username)

        self.token_2 = jwt_encode_handler(jwt_payload_handler(user_2))

        tanggal_kelas = "2016-11-16T22:31:18.130822+00:00"
        mata_kuliah = MataKuliah.objects.create(nama="Aljabar Linier")
        jenis_pengumuman = JenisPengumuman.objects.create(nama="Asistensi")
        ruang = Ruang.objects.create(nama="2311")
        sesi = Sesi.objects.create(nama="Sesi 4 (17.00 - 19.30)")
        status_pengumuman = StatusPengumuman.objects.create(nama="Terlambat")

        self.pengumuman_pk = Pengumuman.objects.create(tanggal_kelas=tanggal_kelas,
                                                       pembuat=user_2, nama_mata_kuliah=mata_kuliah,
                                                       jenis_pengumuman=jenis_pengumuman,
                                                       nama_dosen="Lulu Ilmaknun S.kom",
                                                       nama_asisten="Annida Safira",
                                                       nama_ruang=ruang,
                                                       nama_sesi=sesi,
                                                       nama_status_pengumuman=status_pengumuman,
                                                       komentar="").pk

        self.valid_data = {
            'tanggal_kelas': '2016-11-16',
            'nama_mata_kuliah': 'Aljabar Linier',
            'jenis_pengumuman': 'Asistensi',
            'nama_dosen': 'Dosen Nafis',
            'nama_asisten': 'Nida',
            'nama_ruang': '2311',
            'nama_sesi': 'Sesi 4 (17.00 - 19.30)',
            'nama_status_pengumuman': 'Terlambat',
            'komentar': 'Saya kesiangan'
        }
        self.invalid_data = {
            'tanggal_kelass': '2016-11-12',
        }



    def test_cant_create(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_1)
        response = self.client.post('/api/pengumuman/create/',
                                    data=urlencode(MultiValueDict(self.invalid_data)),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 403)

    def test_can_create(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_2)

        response = self.client.post('/api/pengumuman/create/',
                                    data=urlencode(MultiValueDict(self.valid_data)),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
