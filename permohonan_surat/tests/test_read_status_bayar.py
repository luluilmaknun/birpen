from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from permohonan_surat.models import StatusBayar

from permohonan_surat.views import read_status_bayar

from sso_ui.models import Admin

User = get_user_model()


class ReadStatusBayarApiTest(TestCase):
    def setUp(self):
        user_admin = User.objects.create(username='lulu.ilmaknun',
                                         password='admin')
        Admin.objects.create(username=user_admin.username)

        StatusBayar.objects.create(nama='Belum bayar')

    def test_request_authenticated(self):
        factory = APIRequestFactory()
        view = read_status_bayar
        user = User.objects.get(username='lulu.ilmaknun')

        request = factory.get('/api/permohonan-surat/status-bayar')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_request_unauthenticated(self):
        factory = APIRequestFactory()
        view = read_status_bayar

        request = factory.get('/api/permohonan-surat/status-bayar')
        response = view(request)
        self.assertEqual(response.status_code, 401)
