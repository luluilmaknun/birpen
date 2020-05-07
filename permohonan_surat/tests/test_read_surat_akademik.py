from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from sso_ui.models import Admin

User = get_user_model()


class ReadAllPengumumanTest(TestCase):
    def setUp(self):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        self.client = APIClient()

        self.mahasiswa = User.objects.create(username='annida.safira',
                                             password='nida')
        self.mahasiswa.profile.role = 'mahasiswa'
        self.mahasiswa.profile.save()
        self.token_mahasiswa = jwt_encode_handler(jwt_payload_handler(self.mahasiswa))

        self.alumni = User.objects.create(username='yusuf.tri',
                                          password='yusuf')
        self.alumni.profile.role = 'alumni'
        self.alumni.profile.save()
        self.token_alumni = jwt_encode_handler(jwt_payload_handler(self.alumni))

        self.dosen = User.objects.create(username='ahmad.fauzan',
                                         password='fauzan')
        self.dosen.profile.role = 'staff'
        self.dosen.profile.save()
        self.token_dosen = jwt_encode_handler(jwt_payload_handler(self.dosen))

        self.admin = User.objects.create(username='athallah.annafis',
                                         password='nafis')
        Admin.objects.create(username=self.admin.username)
        self.token_admin = jwt_encode_handler(jwt_payload_handler(self.admin))

    def test_request_without_authentication(self):
        response = self.client.get('/api/permohonan-surat/surat-akademik/')

        self.assertEqual(response.status_code, 401)

    def test_dosen_not_privileged(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_dosen)
        response = self.client.get('/api/permohonan-surat/surat-akademik/')

        self.assertEqual(response.status_code, 403)

    def test_request_as_alumni(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_alumni)
        response = self.client.get('/api/permohonan-surat/surat-akademik/')

        self.assertEqual(response.status_code, 200)

    def test_request_as_mahasiswa(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_mahasiswa)
        response = self.client.get('/api/permohonan-surat/surat-akademik/')

        self.assertEqual(response.status_code, 200)

    def test_request_as_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.get('/api/permohonan-surat/surat-akademik/')

        self.assertEqual(response.status_code, 200)
