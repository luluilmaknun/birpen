from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from sso_ui.models import Admin, AsistenDosen

User = get_user_model()


class ReadAllPengumumanTest(TestCase):
    def setUp(self):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user_1 = User.objects.create(username='julia.ningrum', password='admin')
        Admin.objects.create(username=user_1.username)
        self.token_1 = jwt_encode_handler(jwt_payload_handler(user_1))

        user_2 = User.objects.create(username='lulu.ilmaknun', password='dosen')
        user_2.profile.role = "staff"
        user_2.save()
        self.token_2 = jwt_encode_handler(jwt_payload_handler(user_2))

        user_3 = User.objects.create(username='yusuf.tri', password='mahasiswa')
        self.token_3 = jwt_encode_handler(jwt_payload_handler(user_3))

        AsistenDosen.objects.create(username="Agas Yanpratama")
        AsistenDosen.objects.create(username="Ichlassul Affan")

        self.client = APIClient()


    def test_request_without_authentication(self):
        response = self.client.get('/api/asdos/'.format(10000))

        self.assertEqual(response.status_code, 401)


    def test_request_not_privileged(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_3)
        response = self.client.get('/api/asdos/'.format(10000))

        self.assertEqual(response.status_code, 403)


    def test_request_as_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_1)
        response = self.client.get('/api/asdos/'.format(10000))

        self.assertEqual(response.status_code, 200)

    def test_request_as_dosen(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_2)
        response = self.client.get('/api/asdos/'.format(10000))

        self.assertEqual(response.status_code, 200)
