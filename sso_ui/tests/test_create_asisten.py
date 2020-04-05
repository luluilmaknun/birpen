from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from sso_ui.models import Admin, AsistenDosen

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.mahasiswa = User.objects.create(username='annida.safira',
                                             password='nida')
        self.mahasiswa.profile.role = 'mahasiswa'
        self.token_mahasiswa = Token.objects.get_or_create(user=self.mahasiswa)[0].key
        self.mahasiswa.profile.save()

        self.dosen = User.objects.create(username='ahmad.fauzan',
                                         password='fauzan')
        self.dosen.profile.role = 'staff'
        self.token_dosen = Token.objects.get_or_create(user=self.dosen)[0].key
        self.dosen.profile.save()

        self.admin = User.objects.create(username='julia.ningrum',
                                         password='admin')
        self.token_admin = Token.objects.get_or_create(user=self.admin)[0].key
        Admin.objects.create(username=self.admin.username)

        self.asisten = User.objects.create(username='yusuf.tri',
                                           password='asdos')
        self.token_asisten = Token.objects.get_or_create(user=self.asisten)[0].key
        AsistenDosen.objects.create(username=self.asisten.username)

    def test_admin_create_asisten(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_admin)

        response = self.client.post('/sso/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'username': self.admin.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    def test_mahasiswa_create_asisten(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_mahasiswa)

        response = self.client.post('/sso/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'username': self.mahasiswa.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    def test_asisten_create_asisten(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_asisten)

        response = self.client.post('/sso/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'username': self.asisten.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    def test_dosen_create_asisten(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_dosen)
        response = self.client.post('/sso/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'username': self.dosen.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    def test_invalid_data(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_dosen)

        response = self.client.post('/sso/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'name': self.dosen.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    def test_create_registered_asisten(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_dosen)

        response = self.client.post('/sso/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'username': self.dosen.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)

        response = self.client.post('/sso/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'username': self.dosen.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 400)
    