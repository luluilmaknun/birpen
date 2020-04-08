from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode

from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from sso_ui.models import Admin, AsistenDosen

User = get_user_model()


class DeleteApiTest(TestCase):
    def setUp(self):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        self.client = APIClient()

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

        self.asisten_1 = User.objects.create(username='yusuf.tri1',
                                             password='asdos')
        self.token_asisten_1 = jwt_encode_handler(jwt_payload_handler(self.asisten_1))
        AsistenDosen.objects.create(username=self.asisten_1.username)

        self.asisten_2 = User.objects.create(username='yusuf.tri2',
                                             password='asdos')
        self.token_asisten_2 = jwt_encode_handler(jwt_payload_handler(self.asisten_2))
        AsistenDosen.objects.create(username=self.asisten_2.username)

    def test_no_asisten_found(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.delete('/api/asdos/delete/',
                                      data=urlencode(MultiValueDict({
                                          'username': 'lulu.ilmaknun'
                                      })),
                                      content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.data['detail'], 'Asisten does not exist.')

    def test_mahasiswa_delete_asisten(self):
        before_delete_count = AsistenDosen.objects.all().count()

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_mahasiswa)
        response = self.client.delete('/api/asdos/delete/',
                                      data=urlencode(MultiValueDict({
                                          'username': self.asisten_1.username
                                      })),
                                      content_type='application/x-www-form-urlencoded')

        self.assertEqual(before_delete_count, AsistenDosen.objects.all().count())
        self.assertEqual(response.status_code, 403)

    def test_admin_delete_asisten(self):
        before_delete_count = AsistenDosen.objects.all().count()

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.delete('/api/asdos/delete/',
                                      data=urlencode(MultiValueDict({
                                          'username': self.asisten_1.username
                                      })),
                                      content_type='application/x-www-form-urlencoded')

        self.assertEqual(before_delete_count, AsistenDosen.objects.all().count() + 1)
        self.assertEqual(response.status_code, 200)

    def test_dosen_delete_asisten(self):
        before_delete_count = AsistenDosen.objects.all().count()

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_dosen)
        response = self.client.delete('/api/asdos/delete/',
                                      data=urlencode(MultiValueDict({
                                          'username': self.asisten_2.username
                                      })),
                                      content_type='application/x-www-form-urlencoded')

        self.assertEqual(before_delete_count, AsistenDosen.objects.all().count() + 1)
        self.assertEqual(response.status_code, 200)
