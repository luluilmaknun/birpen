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
        user = get_user_model()
        user.objects.create_user(username='yusuf.tri',
                                 name='yusuf tri a.', npm='1701837382', password='mahasiswa', user_type=1)
        user.objects.create_user(username='athallah.annafis',
                                 name='athallah annafis.', npm='1706492028', password='asdos',user_type= 2)
        user.objects.create_user(username='ahmad.fauzan',
                                 name='ahmad fauzan dst.', npm='1102939504', password='dosen', user_type=3)
        user.objects.create_user(username='julia.ningrum',
                                 name='julia ningrum', npm='12048593059', password='admin', user_type=4)



    def test_login_as_mhs(self):
        pwd = "mahasiswa"
        client = APIClient()
        response = client.login(username="yusuf.tri", password=pwd)
        self.assertEqual(response, True)

    def test_login_as_asdos(self):
        client = APIClient()
        response = client.login(username="athallah.annafis", password="asdos")
        self.assertEqual(response, True)

    def test_login_as_dosen(self):
        client = APIClient()
        response = client.login(username="ahmad.fauzan", password="dosen")
        self.assertEqual(response,True)

    def test_login_as_admin(self):
        client = APIClient()
        response = client.login(username="julia.ningrum", password="admin")
        self.assertEqual(response, True)

    def test_login_failed(self):
        client = APIClient()
        response = client.login(username="annida.safira", password="admin")
        self.assertEqual(response, False)