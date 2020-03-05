from datetime import datetime

from django.apps import apps
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from pengumuman.apps import PengumumanConfig
from .models import MataKuliah, JenisPengumuman, Ruang, Sesi, StatusPengumuman, Pengumuman, \
    User
from .views import dropdown_pengumuman, filter_pengumuman


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


class LoginTest(TestCase):
    def setUp(self):
        user = get_user_model()
        user.objects.create_user(username='yusuf.tri',
                                 name='yusuf tri a.', npm='1701837382',
                                 password='mahasiswa', user_type=User.MAHASISWA)
        user.objects.create_user(username='athallah.annafis',
                                 name='athallah annafis.', npm='1706492028',
                                 password='asdos', user_type=User.ASDOS)
        user.objects.create_user(username='ahmad.fauzan',
                                 name='ahmad fauzan dst.', npm='1102939504',
                                 password='dosen', user_type=User.DOSEN)
        user.objects.create_user(username='julia.ningrum',
                                 name='julia ningrum', npm='1204893059',
                                 password='admin', user_type=User.ADMIN)

    def test_login_as_mhs(self):
        client = APIClient()
        response = client.login(username="yusuf.tri", password="mahasiswa")
        self.assertEqual(response, True)

    def test_login_as_asdos(self):
        client = APIClient()
        response = client.login(username="athallah.annafis", password="asdos")
        self.assertEqual(response, True)

    def test_login_as_dosen(self):
        client = APIClient()
        response = client.login(username="ahmad.fauzan", password="dosen")
        self.assertEqual(response, True)

    def test_login_as_admin(self):
        client = APIClient()
        response = client.login(username="julia.ningrum", password="admin")
        self.assertEqual(response, True)

    def test_login_failed(self):
        client = APIClient()
        response = client.login(username="annida.safira", password="admin")
        self.assertEqual(response, False)

    def test_post_login_success(self):
        client = APIClient()
        response = client.post('/api/pengumuman/login',
                               data=urlencode(MultiValueDict(({
                                   'username': 'yusuf.tri', 'password': 'mahasiswa'}))),
                               content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    def test_post_login_blank(self):
        client = APIClient()
        response = client.post('/api/pengumuman/login',
                               data=urlencode(MultiValueDict(({'username': 'yusuf.tri'}))),
                               content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    def test_post_login_invalid(self):
        client = APIClient()
        response = client.post('/api/pengumuman/login',
                               data=urlencode(MultiValueDict(({
                                   'username': 'annida.safira', 'password': 'hehehehe'}))),
                               content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 404)

    def test_login_form(self):
        client = APIClient()
        response = client.get('/api/pengumuman/login')
        self.assertIn("Login Dummy", response.content.decode("utf8"))


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
        user = User.objects.create(username='julia.ningrum', name='julia ningrum',
                                   npm='1204893059', password='admin', user_type=User.ADMIN)

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
        user = User.objects.create(username='julia.ningrum', name='julia ningrum',
                                   npm='1204893059', password='admin', user_type=User.ADMIN)

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


class FilterPengumumanTest(TestCase):
    def setUp(self):
        tanggal_kelas = "2016-11-16T07:00:18.130822+00:00"
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

class DropdownApiTest(TestCase):
    def setUp(self):
        User.objects.create(username='julia.ningrum', name='julia ningrum',
                            npm='1204893059', password='admin', user_type=User.ADMIN)
        User.objects.create(username='yusuf.tri',
                            name='yusuf tri a.', npm='1701837382',
                            password='mahasiswa', user_type=User.MAHASISWA)

    def test_request_as_admin(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='julia.ningrum')
        view = dropdown_pengumuman

        JenisPengumuman.objects.create(nama='Asistensi')
        MataKuliah.objects.create(nama='Sistem Cerdas')
        Ruang.objects.create(nama='3111')
        Sesi.objects.create(nama='Sesi 1 (08.00 - 10.30)')
        StatusPengumuman.objects.create(nama='Terlambat')

        # Make an authenticated request to the view...
        request = factory.get('/api/pengumuman/dropdown')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)


class DeleteApiTest(TestCase):
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
