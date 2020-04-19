from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode

from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from sso_ui.models import Admin, AsistenDosen

User = get_user_model()


class CreateAdminTest(TestCase):
    def setUp(self):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        self.client = APIClient()

        self.mahasiswa = User.objects.create(username='annida.safira',
                                             password='nida')
        self.mahasiswa.profile.role = 'mahasiswa'
        self.mahasiswa.profile.save()

        self.token_mahasiswa = jwt_encode_handler(jwt_payload_handler(self.mahasiswa))

        self.dosen = User.objects.create(username='ahmad.fauzan',
                                         password='fauzan')
        self.dosen.profile.role = 'staff'
        self.dosen.profile.save()
        self.token_dosen = jwt_encode_handler(jwt_payload_handler(self.dosen))

        self.admin = User.objects.create(username='athallah.annafis',
                                         password='admin')
        Admin.objects.create(username=self.admin.username)
        self.token_admin = jwt_encode_handler(jwt_payload_handler(self.admin))

        self.asisten = User.objects.create(username='yusuf.tri',
                                           password='asdos')
        AsistenDosen.objects.create(username=self.asisten.username)
        self.token_asisten = jwt_encode_handler(jwt_payload_handler(self.asisten))

    def test_username_not_provided(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.post('/api/admin_birpen/create/',
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Username not provided.')

    def test_admin_already_exists(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.post('/api/admin_birpen/create/',
                                    data=urlencode(MultiValueDict({
                                        'username': self.admin.username
                                    })),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Admin already exists.')

    def test_username_too_long(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.post('/api/admin_birpen/create/',
                                    data=urlencode(MultiValueDict({
                                        'username': "a" * 151
                                    })),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Invalid username.')

    def test_mahasiswa_cant_create_admin(self):
        before_delete_count = Admin.objects.all().count()

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_mahasiswa)
        response = self.client.post('/api/admin_birpen/create/',
                                    data=urlencode(MultiValueDict({
                                        'username': 'lulu.ilmaknun'
                                    })),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(before_delete_count, Admin.objects.all().count())
        self.assertEqual(response.status_code, 403)

    def test_asdos_cant_create_admin(self):
        before_delete_count = Admin.objects.all().count()

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_asisten)
        response = self.client.post('/api/admin_birpen/create/',
                                    data=urlencode(MultiValueDict({
                                        'username': 'lulu.ilmaknun'
                                    })),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(before_delete_count, Admin.objects.all().count())
        self.assertEqual(response.status_code, 403)

    def test_dosen_cant_create_admin(self):
        before_delete_count = Admin.objects.all().count()

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_dosen)
        response = self.client.post('/api/admin_birpen/create/',
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(before_delete_count, Admin.objects.all().count())
        self.assertEqual(response.status_code, 403)

    def test_admin_can_create_admin(self):
        before_delete_count = Admin.objects.all().count()

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.post('/api/admin_birpen/create/',
                                    data=urlencode(MultiValueDict({
                                        'username': 'lulu.ilmaknun'
                                    })),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(before_delete_count + 1, Admin.objects.all().count())
        self.assertEqual(response.status_code, 200)
