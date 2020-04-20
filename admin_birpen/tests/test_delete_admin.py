from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from sso_ui.models import Admin, AsistenDosen

User = get_user_model()


class DeleteAdminTest(TestCase):
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

        self.admin_1 = User.objects.create(username='athallah.annafis',
                                           password='admin')
        Admin.objects.create(username=self.admin_1.username)
        self.token_admin_1 = jwt_encode_handler(jwt_payload_handler(self.admin_1))

        self.admin_2 = User.objects.create(username='lulu.ilmaknun',
                                           password='admin')
        Admin.objects.create(username=self.admin_2.username)
        self.token_admin_2 = jwt_encode_handler(jwt_payload_handler(self.admin_2))

        self.asisten = User.objects.create(username='yusuf.tri',
                                           password='asdos')
        AsistenDosen.objects.create(username=self.asisten.username)
        self.token_asisten = jwt_encode_handler(jwt_payload_handler(self.asisten))

    def test_delete_target_admin_not_found(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin_1)
        response = self.client.delete('/api/admin_birpen/alya.zahra/delete/',
                                      content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.data['detail'], 'Admin does not exist.')

    def test_mahasiswa_cant_delete_admin(self):
        before_delete_count = Admin.objects.all().count()

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_mahasiswa)
        response = self.client.delete('/api/admin_birpen/' +  self.admin_2.username +'/delete/',
                                      content_type='application/x-www-form-urlencoded')

        self.assertEqual(before_delete_count, Admin.objects.all().count())
        self.assertEqual(response.status_code, 403)

    def test_asdos_cant_delete_admin(self):
        before_delete_count = Admin.objects.all().count()

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_asisten)
        response = self.client.delete('/api/admin_birpen/' + self.admin_2.username +'/delete/',
                                      content_type='application/x-www-form-urlencoded')

        self.assertEqual(before_delete_count, Admin.objects.all().count())
        self.assertEqual(response.status_code, 403)

    def test_dosen_cant_delete_admin(self):
        before_delete_count = Admin.objects.all().count()

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_dosen)
        response = self.client.delete('/api/admin_birpen/' + self.admin_2.username + '/delete/',
                                      content_type='application/x-www-form-urlencoded')

        self.assertEqual(before_delete_count, Admin.objects.all().count())
        self.assertEqual(response.status_code, 403)

    def test_admin_can_delete_admin(self):
        before_delete_count = Admin.objects.all().count()

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin_1)
        response = self.client.delete('/api/admin_birpen/' + self.admin_2.username + '/delete/',
                                      content_type='application/x-www-form-urlencoded')

        self.assertEqual(before_delete_count, Admin.objects.all().count() + 1)
        self.assertEqual(response.status_code, 200)
