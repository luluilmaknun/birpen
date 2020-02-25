from django.apps import apps
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from pengumuman.apps import PengumumanConfig
from django.contrib.auth import get_user_model


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
        User = get_user_model()
        User.objects.create_user('yusuf.tri',
                                 'yusuf tri a.', '1701837382', 'mahasiswa', 1)
        User.objects.create_user('athallah.annafis',
                                 'athallah annafis.', '1706492028', 'asdos', 2)
        User.objects.create_user('ahmad.fauzan',
                                 'ahmad fauzan dst.', '1102939504', 'dosen', 3)
        User.objects.create_user('julia.ningrum',
                                 'julia ningrum', '12048593059', 'admin', 4)

    def test_login_page(self):
        response = APIClient().get('/api/pengumuman/login')
        self.assertEqual(response.status_code, 200)

    def test_login_as_mhs(self):
        pwd = "mahasiswa"
        client = APIClient()
        response = APIClient().get('/api/pengumuman/login')
        client.login(username="yusuf.tri", password=pwd)
        self.assertEqual(response.status_code, 200)

    def test_login_as_asdos(self):
        client = APIClient()
        response = APIClient().get('/api/pengumuman/login')
        client.login(username="athallah.annafis", password="asdos")
        self.assertEqual(response.status_code, 200)

    def test_login_as_dosen(self):
        client = APIClient()
        response = APIClient().get('/api/pengumuman/login')
        client.login(username="ahmad.fauzan", password="dosen")
        self.assertEqual(response.status_code, 200)

    def test_login_as_admin(self):
        client = APIClient()
        response = APIClient().get('/api/pengumuman/login')
        client.login(username="julia.ningrum", password="admin")
        self.assertEqual(response.status_code, 200)
