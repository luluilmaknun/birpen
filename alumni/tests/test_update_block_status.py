from django.contrib.auth import get_user_model
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode
from django.test import TestCase

from rest_framework.test import APIClient

from rest_framework_jwt.settings import api_settings

from admin_birpen.models import Admin

User = get_user_model()

class RegisterAlumniTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user_admin = User.objects.create(username='athallah.annafis', password='admin')
        Admin.objects.create(username=user_admin.username)
        self.token_admin = jwt_encode_handler(jwt_payload_handler(user_admin))

        user_non_admin = User.objects.create(username='ahmad.fauzan', password='not_admin')
        self.token_non_admin = jwt_encode_handler(jwt_payload_handler(user_non_admin))

        self.alumni = User.objects.create(username='annida.safira',
                                          password='nida')
        self.alumni.profile.role = 'alumni'
        self.alumni.profile.save()

        self.user_non_alumni = User.objects.create(username='yusuf.tri',
                                                   password='yusuf')

    def test_request_without_authentication(self):
        response = self.client.patch('/api/alumni/' + self.alumni.username + '/block/',
                                     content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(response.status_code, 401)

    def test_user_non_admin_cant_access(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_non_admin)
        response = self.client.patch('/api/alumni/' + self.alumni.username + '/block/',
                                     data=urlencode(MultiValueDict({
                                         'is_blocked': True,
                                     })),
                                     content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'],
                         'You do not have permission to perform this action.')
        self.assertEqual(response.status_code, 403)

    def test_invalid_data_no_is_blocked(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.patch('/api/alumni/' + self.alumni.username + '/block/',
                                     content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Invalid data.')
        self.assertEqual(response.status_code, 400)

    def test_invalid_data_is_blocked_not_boolean(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.patch('/api/alumni/' + self.alumni.username + '/block/',
                                     data=urlencode(MultiValueDict({
                                         'is_blocked': 'not_boolean',
                                     })),
                                     content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Invalid data.')
        self.assertEqual(response.status_code, 400)

    def test_invalid_data_user_not_found(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.patch('/api/alumni/ahmad.fauzan/block/',
                                     content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Alumni does not exist.')
        self.assertEqual(response.status_code, 400)

    def test_invalid_data_user_non_alumni(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.patch('/api/alumni/' + self.user_non_alumni.username + '/block/',
                                     content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Alumni does not exist.')
        self.assertEqual(response.status_code, 400)

    def test_success_block(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.patch('/api/alumni/' + self.alumni.username + '/block/',
                                     data=urlencode(MultiValueDict({
                                         'is_blocked': True,
                                     })),
                                     content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.status_code, 200)

    def test_success_unblock(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.patch('/api/alumni/' + self.alumni.username + '/block/',
                                     data=urlencode(MultiValueDict({
                                         'is_blocked': False,
                                     })),
                                     content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.status_code, 200)
