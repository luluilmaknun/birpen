from django.test import TestCase
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from pengumuman.models import MataKuliah, JenisPengumuman, Ruang, \
    Sesi, StatusPengumuman, Pengumuman, User

class CreateApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        user_1 = User.objects.create(username='athallah.annafis', name='Athallah Annafis',
                                     npm='1701837382', password='mahasiswa',
                                     user_type=User.MAHASISWA)
        self.token_1 = Token.objects.get_or_create(user=user_1)[0].key

        user_2 = User.objects.create(username='julia.ningrum', name='Julia Ningrum',
                                     npm='1204893059', password='admin', user_type=User.ADMIN)
        self.token_2 = Token.objects.get_or_create(user=user_2)[0].key

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
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_1)
        response = self.client.post('/api/pengumuman/create/',
                                    data=urlencode(MultiValueDict(self.invalid_data)),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    def test_can_create(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_1)

        response = self.client.post('/api/pengumuman/create/',
                                    data=urlencode(MultiValueDict(self.valid_data)),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    def test_no_announcement_found(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_1)
        response = self.client.post('/api/pengumuman/{}/delete/'.format('999'))

        self.assertEqual(response.data['detail'], 'Pengumuman does not exist.')

    def test_not_owner_of_announcement(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_1)
        response = self.client.post('/api/pengumuman/{}/delete/'.format(self.pengumuman_pk))

        self.assertEqual(response.data['detail'], 'You are not the owner of the announcement.')

    def test_success_delete(self):
        before_delete_count = Pengumuman.objects.all().count()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_2)
        response = self.client.post('/api/pengumuman/{}/delete/'.format(self.pengumuman_pk))

        self.assertEqual(before_delete_count, Pengumuman.objects.all().count()+1)
        self.assertEqual(response.status_code, 200)
