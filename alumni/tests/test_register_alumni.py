from django.contrib.auth import get_user_model
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode
from django.test import TestCase
from rest_framework.test import APIClient

User = get_user_model()

class RegisterAlumniTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.alumni = User.objects.create(username='@annida.safira',
                                          password='nida')
        self.alumni.profile.role = 'alumni'
        self.alumni.profile.save()

    def test_invalid_data_no_username(self):
        response = self.client.post('/api/alumni/register/',
                                    data=urlencode(MultiValueDict({
                                        'password': 'sample_password',
                                        'email': 'sample_email'
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Username, email, atau password tidak valid')
        self.assertEqual(response.status_code, 400)

    def test_invalid_data_no_password(self):
        response = self.client.post('/api/alumni/register/',
                                    data=urlencode(MultiValueDict({
                                        'username': '@sample_username',
                                        'email': 'sample_email'
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Username, email, atau password tidak valid')
        self.assertEqual(response.status_code, 400)

    def test_invalid_data_no_email(self):
        response = self.client.post('/api/alumni/register/',
                                    data=urlencode(MultiValueDict({
                                        'username': '@sample_username',
                                        'password': 'sample_password',
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Username, email, atau password tidak valid')
        self.assertEqual(response.status_code, 400)

    def test_invalid_data_blank_password(self):
        response = self.client.post('/api/alumni/register/',
                                    data=urlencode(MultiValueDict({
                                        'username': '@sample_username',
                                        'password': '',
                                        'email': 'sample_email'
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Username, email, atau password tidak valid')
        self.assertEqual(response.status_code, 400)

    def test_invalid_data_blank_username(self):
        response = self.client.post('/api/alumni/register/',
                                    data=urlencode(MultiValueDict({
                                        'username': '',
                                        'password': 'sample_password',
                                        'email': 'sample_email'
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Username, email, atau password tidak valid')
        self.assertEqual(response.status_code, 400)

    def test_invalid_data_blank_email(self):
        response = self.client.post('/api/alumni/register/',
                                    data=urlencode(MultiValueDict({
                                        'username': '@sample_username',
                                        'password': 'sample_password',
                                        'email': ''
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Username, email, atau password tidak valid')
        self.assertEqual(response.status_code, 400)

    def test_invalid_data_long_username(self):
        response = self.client.post('/api/alumni/register/',
                                    data=urlencode(MultiValueDict({
                                        'username': 'a'*151,
                                        'password': 'sample_password',
                                        'email': 'sample_email'
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Username, email, atau password tidak valid')
        self.assertEqual(response.status_code, 400)

    def test_register_registered_asisten(self):
        response = self.client.post('/api/alumni/register/',
                                    data=urlencode(MultiValueDict({
                                        'username': self.alumni.username,
                                        'password': 'sample_password',
                                        'email': 'sample_email'
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Username sudah terdaftar')
        self.assertEqual(response.status_code, 400)

    def test_username_prefix_invalid(self):
        response = self.client.post('/api/alumni/register/',
                                    data=urlencode(MultiValueDict({
                                        'username': 'sample_username',
                                        'password': 'sample_password',
                                        'email': 'sample_email'
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Username, email, atau password tidak valid')

    def test_success_register_asisten(self):
        response = self.client.post('/api/alumni/register/',
                                    data=urlencode(MultiValueDict({
                                        'username': '@sample_username',
                                        'password': 'sample_password',
                                        'email': 'sample_email'
                                    })),
                                    content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.status_code, 200)
