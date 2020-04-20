from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from admin_birpen.models import Admin

User = get_user_model()


class ReadAllAlumniTest(TestCase):
    def setUp(self):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user_admin = User.objects.create(username='athallah.annafis', password='admin')
        Admin.objects.create(username=user_admin.username)
        self.token_admin = jwt_encode_handler(jwt_payload_handler(user_admin))

        user_non_admin = User.objects.create(username='yusuf.tri', password='non_admin')
        self.token_non_admin = jwt_encode_handler(jwt_payload_handler(user_non_admin))

        alumni_1 = User.objects.create(username='lulu.ilmaknun', email='lulu@gmail.com',
                                       password='lulu')
        alumni_1.profile.role = 'alumni'
        alumni_1.profile.save()

        alumni_2 = User.objects.create(username='annida.safira', email='nida@gmail.com',
                                       password='nida')
        alumni_2.profile.role = 'alumni'
        alumni_2.profile.save()

        self.client = APIClient()


    def test_request_without_authentication(self):
        response = self.client.get('/api/alumni/')

        self.assertEqual(response.status_code, 401)


    def test_request_not_privileged(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_non_admin)
        response = self.client.get('/api/alumni/')

        self.assertEqual(response.status_code, 403)


    def test_request_as_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.get('/api/alumni/')

        self.assertEqual(response.status_code, 200)
