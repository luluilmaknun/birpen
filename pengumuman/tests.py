from django.apps import apps
from django.contrib.auth import get_user_model
from django.test import TestCase

from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode

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


class login_test(TestCase):
    def setUp(self):
        user = get_user_model()
        user.objects.create_user(username='yusuf.tri',
                                 name='yusuf tri a.', npm='1701837382',
                                 password='mahasiswa', user_type=1)
        user.objects.create_user(username='athallah.annafis',
                                 name='athallah annafis.', npm='1706492028',
                                 password='asdos', user_type=2)
        user.objects.create_user(username='ahmad.fauzan',
                                 name='ahmad fauzan dst.', npm='1102939504',
                                 password='dosen', user_type=3)
        user.objects.create_user(username='julia.ningrum',
                                 name='julia ningrum', npm='1204893059',
                                 password='admin', user_type=4)



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
        print(response)
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
