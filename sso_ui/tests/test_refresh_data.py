from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

User = get_user_model()


class RefreshDataTest(TestCase):
    def setUp(self):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        self.client = APIClient()

        self.user = User.objects.create(username='athallah.annafis', password='nafis')
        self.user.save()
        self.token = jwt_encode_handler(jwt_payload_handler(self.user))

    def test_not_authenticated(self):
        response = self.client.get('/sso/refresh-data/')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

    def test_success_refresh_data(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get('/sso/refresh-data/')

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data['token'])
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['role'], self.user.profile.role)
        self.assertEqual(response.data['is_asdos'], self.user.is_asdos())
        self.assertEqual(response.data['is_admin'], self.user.is_admin())
