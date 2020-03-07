from datetime import datetime

from django.test import TestCase
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from pengumuman.models import MataKuliah, JenisPengumuman, Ruang, \
    Sesi, StatusPengumuman, Pengumuman, User


class PengumumanApiTest(TestCase):
    def setUp(self):
        user_1 = User.objects.create(username='athallah.annafis', name='Athallah Annafis',
                                     npm='1701837382', password='mahasiswa',
                                     user_type=User.MAHASISWA)
        self.token_1 = Token.objects.get_or_create(user=user_1)[0].key

        user_2 = User.objects.create(username='julia.ningrum', name='Julia Ningrum',
                                     npm='1204893059', password='admin', user_type=User.ADMIN)
        self.token_2 = Token.objects.get_or_create(user=user_2)[0].key

        user_3 = User.objects.create(username='yusuf.tri', name='Yusuf Tri Ardho',
                                     npm='1701837382', password='mahasiswa',
                                     user_type=User.MAHASISWA)
        self.token_3 = Token.objects.get_or_create(user=user_3)[0].key

        tanggal_kelas = "2016-11-16T22:31:18.130822+00:00"
        mata_kuliah = MataKuliah.objects.create(nama="Aljabar Linier")
        jenis_pengumuman = JenisPengumuman.objects.create(nama="Asistensi")
        ruang = Ruang.objects.create(nama="2311")
        sesi = Sesi.objects.create(nama="Sesi 4 (17.00 - 19.30)")
        status_pengumuman = StatusPengumuman.objects.create(nama="Terlambat")

        self.pengumuman = Pengumuman.objects.create(tanggal_kelas=tanggal_kelas,
                                                    pembuat=user_3, nama_mata_kuliah=mata_kuliah,
                                                    jenis_pengumuman=jenis_pengumuman,
                                                    nama_dosen="Lulu Ilmaknun S.kom",
                                                    nama_asisten="Annida Safira",
                                                    nama_ruang=ruang,
                                                    nama_sesi=sesi,
                                                    nama_status_pengumuman=status_pengumuman,
                                                    komentar="")

        self.pengumuman_pk = self.pengumuman.pk

        mata_kuliah = MataKuliah.objects.create(nama="DDP")
        jenis_pengumuman = JenisPengumuman.objects.create(nama="Perkuliahan")
        ruang = Ruang.objects.create(nama="3311")
        sesi = Sesi.objects.create(nama="Sesi 4 (17.00 - 19.25)")
        status_pengumuman = StatusPengumuman.objects.create(nama="Dibatalkan")

        self.valid_data = {
            'tanggal_kelas': '2016-11-12',
            'nama_mata_kuliah': 'DDP',
            'jenis_pengumuman': 'Perkuliahan',
            'nama_dosen': 'Dosen Baru',
            'nama_ruang': '3311',
            'nama_sesi': 'Sesi 4 (17.00 - 19.25)',
            'nama_status_pengumuman': 'Dibatalkan'
        }

        self.client = APIClient()

    def test_fail_edit_without_authorization_header(self):
        response = self.client.post('/api/pengumuman/{}/edit/'.format(self.pengumuman_pk),
                                    data=urlencode(MultiValueDict(())),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

    def test_fail_edit_with_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token invalid_token')
        response = self.client.post('/api/pengumuman/{}/edit/'.format(self.pengumuman_pk),
                                    data=urlencode(MultiValueDict(self.valid_data)),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(str(response.data['detail']), 'Invalid token.')

    def test_fail_edit_because_pengumuman_doesnt_exist(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_1)
        response = self.client.post('/api/pengumuman/{}/edit/'.format(100),
                                    data=urlencode(MultiValueDict(self.valid_data)),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Pengumuman does not exist.')

    def test_fail_edit_because_not_enough_privileges(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_1)
        response = self.client.post('/api/pengumuman/{}/edit/'.format(self.pengumuman_pk),
                                    data=urlencode(MultiValueDict((self.valid_data))),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Not enough privileges.')

    def test_fail_edit_because_invalid_data(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_3)
        invalid_nama_mata_kuliah = "Aljabar Linierisss"

        invalid_data = self.valid_data
        invalid_data['nama_mata_kuliah'] = invalid_nama_mata_kuliah

        response = self.client.post('/api/pengumuman/{}/edit/'.format(self.pengumuman_pk),
                                    data=urlencode(MultiValueDict((invalid_data))),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Invalid data.')

    def test_success_edit_admin_non_creator(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_2)
        response = self.client.post('/api/pengumuman/{}/edit/'.format(self.pengumuman_pk),
                                    data=urlencode(MultiValueDict(self.valid_data)),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['pengumuman']['tanggal_kelas'],
                         datetime.strptime('2016-11-12', '%Y-%m-%d').date())
        self.assertEqual(response.data['pengumuman']['nama_mata_kuliah'], 'DDP')
        self.assertEqual(response.data['pengumuman']['jenis_pengumuman'], 'Perkuliahan')
        self.assertEqual(response.data['pengumuman']['nama_dosen'], 'Dosen Baru')
        self.assertEqual(response.data['pengumuman']['nama_ruang'], '3311')
        self.assertEqual(response.data['pengumuman']['nama_sesi'], 'Sesi 4 (17.00 - 19.25)')
        self.assertEqual(response.data['pengumuman']['nama_status_pengumuman'], 'Dibatalkan')

    def test_success_edit_pengumuman_creator(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_3)
        response = self.client.post('/api/pengumuman/{}/edit/'.format(self.pengumuman_pk),
                                    data=urlencode(MultiValueDict(self.valid_data)),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['pengumuman']['tanggal_kelas'],
                         datetime.strptime('2016-11-12', '%Y-%m-%d').date())
        self.assertEqual(response.data['pengumuman']['nama_mata_kuliah'], 'DDP')
        self.assertEqual(response.data['pengumuman']['jenis_pengumuman'], 'Perkuliahan')
        self.assertEqual(response.data['pengumuman']['nama_dosen'], 'Dosen Baru')
        self.assertEqual(response.data['pengumuman']['nama_ruang'], '3311')
        self.assertEqual(response.data['pengumuman']['nama_sesi'], 'Sesi 4 (17.00 - 19.25)')
        self.assertEqual(response.data['pengumuman']['nama_status_pengumuman'], 'Dibatalkan')

    def test_success_get_pengumuman_admin(self):
        self.pengumuman.delete()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_2)
        response = self.client.post('/api/pengumuman/{}/'.format(self.pengumuman_pk))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['pengumuman']['tanggal_kelas'],
                         datetime.strptime('2016-11-16', '%Y-%m-%d').date())
        self.assertEqual(response.data['pengumuman']['nama_mata_kuliah'], 'Aljabar Linier')
        self.assertEqual(response.data['pengumuman']['jenis_pengumuman'], 'Asistensi')
        self.assertEqual(response.data['pengumuman']['nama_dosen'], 'Lulu Ilmaknun S.kom')
        self.assertEqual(response.data['pengumuman']['nama_asisten'], 'Annida Safira')
        self.assertEqual(response.data['pengumuman']['nama_ruang'], '2311')
        self.assertEqual(response.data['pengumuman']['nama_sesi'], 'Sesi 4 (17.00 - 19.30)')
        self.assertEqual(response.data['pengumuman']['nama_status_pengumuman'], 'Terlambat')

    def test_fail_get_pengumuman_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_2)
        response = self.client.post('/api/pengumuman/{}/'.format(10000))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Pengumuman does not exist.')

    def test_success_get_pengumuman_non_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_3)
        response = self.client.post('/api/pengumuman/{}/'.format(self.pengumuman_pk))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['pengumuman']['tanggal_kelas'],
                         datetime.strptime('2016-11-16', '%Y-%m-%d').date())
        self.assertEqual(response.data['pengumuman']['nama_mata_kuliah'], 'Aljabar Linier')
        self.assertEqual(response.data['pengumuman']['jenis_pengumuman'], 'Asistensi')
        self.assertEqual(response.data['pengumuman']['nama_dosen'], 'Lulu Ilmaknun S.kom')
        self.assertEqual(response.data['pengumuman']['nama_asisten'], 'Annida Safira')
        self.assertEqual(response.data['pengumuman']['nama_ruang'], '2311')
        self.assertEqual(response.data['pengumuman']['nama_sesi'], 'Sesi 4 (17.00 - 19.30)')
        self.assertEqual(response.data['pengumuman']['nama_status_pengumuman'], 'Terlambat')

    def test_fail_get_pengumuman_non_admin(self):
        self.pengumuman.delete()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_3)
        response = self.client.post('/api/pengumuman/{}/'.format(self.pengumuman_pk))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Pengumuman does not exist.')
