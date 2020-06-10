from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode

from rest_framework.test import APIClient

User = get_user_model()

class LoginTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='ahmad.fauzan71')
        user.set_password('mahasiswa')
        user.save()

        blocked_user = User.objects.create(username='yusuf.tri71', blocked=True)
        blocked_user.set_password('blocked_user')
        blocked_user.save()

    def test_post_login_success(self):
        client = APIClient()
        response = client.post('/sso/obtain-user-info/',
                               data=urlencode(MultiValueDict({
                                   'username': 'ahmad.fauzan71',
                                   'password': 'mahasiswa',
                               })),
                               content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'ahmad.fauzan71')
        self.assertEqual(response.data['role'], '')
        self.assertFalse(response.data['is_admin'])
        self.assertFalse(response.data['is_asdos'])

    def test_credentials_not_provided(self):
        client = APIClient()
        response = client.post('/sso/obtain-user-info/',
                               data=urlencode(MultiValueDict({
                                   'username': 'yusuf.tri',
                               })),
                               content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Please provide both username and password.')


    def test_credentials_invalid(self):
        client = APIClient()
        response = client.post('/sso/obtain-user-info/',
                               data=urlencode(MultiValueDict({
                                   'username': 'athallah.annafis',
                                   'password': 'hehehehe',
                               })),
                               content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data['detail'], 'Invalid credentials.')

    def test_user_has_been_blocked(self):
        client = APIClient()
        response = client.post('/sso/obtain-user-info/',
                               data=urlencode(MultiValueDict({
                                   'username': 'yusuf.tri71',
                                   'password': 'blocked_user',
                               })),
                               content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Account has been blocked by administrator.')
