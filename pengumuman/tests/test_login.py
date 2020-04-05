from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode

from rest_framework.test import APIClient

from pengumuman.models import User


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
