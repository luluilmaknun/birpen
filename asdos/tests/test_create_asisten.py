from django.contrib.auth import get_user_model
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from sso_ui.models import Admin, AsistenDosen

User = get_user_model()

class CreateAsistenTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        self.mahasiswa = User.objects.create(username='annida.safira',
                                             password='nida')
        self.mahasiswa.profile.role = 'mahasiswa'
        self.token_mahasiswa = jwt_encode_handler(jwt_payload_handler(self.mahasiswa))
        self.mahasiswa.profile.save()

        self.dosen = User.objects.create(username='ahmad.fauzan',
                                         password='fauzan')
        self.dosen.profile.role = 'staff'
        self.token_dosen = jwt_encode_handler(jwt_payload_handler(self.dosen))
        self.dosen.profile.save()

        self.admin = User.objects.create(username='julia.ningrum',
                                         password='admin')
        self.token_admin = jwt_encode_handler(jwt_payload_handler(self.admin))
        Admin.objects.create(username=self.admin.username)

        self.asisten = User.objects.create(username='yusuf.tri',
                                           password='asdos')
        self.token_asisten = jwt_encode_handler(jwt_payload_handler(self.asisten))
        AsistenDosen.objects.create(username=self.asisten.username)

    def test_admin_create_asisten(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)

        response = self.client.post('/api/asdos/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'username': self.admin.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    def test_mahasiswa_create_asisten(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_mahasiswa)

        response = self.client.post('/api/asdos/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'username': self.mahasiswa.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 403)

    def test_asisten_create_asisten(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_asisten)

        response = self.client.post('/api/asdos/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'username': self.asisten.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 403)

    def test_dosen_create_asisten(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_dosen)
        response = self.client.post('/api/asdos/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'username': self.dosen.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    def test_invalid_data_no_username(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_dosen)

        response = self.client.post('/api/asdos/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'name': self.dosen.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    def test_invalid_data_blank_username(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_dosen)

        response = self.client.post('/api/asdos/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'username': ''
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    def test_invalid_data_long_username(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_dosen)

        response = self.client.post('/api/asdos/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'username': 'a'*33
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    def test_create_registered_asisten(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_dosen)

        response = self.client.post('/api/asdos/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'username': self.dosen.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)

        response = self.client.post('/api/asdos/create-asisten/',
                                    data=urlencode(MultiValueDict({
                                        'username': self.dosen.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 400)
