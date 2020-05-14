from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from asdos.models import AsistenDosen
from permohonan_surat.models import StatusSurat

from permohonan_surat.views import get_status_surat

from sso_ui.models import Admin

User = get_user_model()


class GetStatusSuratApiTest(TestCase):
    def setUp(self):
        user_admin = User.objects.create(username='admin',
                                         password='admin')
        Admin.objects.create(username=user_admin.username)

        user_asdos = User.objects.create(username='asdos',
                                         password='asdos')
        AsistenDosen.objects.create(username=user_asdos.username)

        user_alumni = User.objects.create(username='alumni',
                                          password='alumni')
        user_alumni.profile.role = 'alumni'

        user_dosen = User.objects.create(username='dosen',
                                         password='dosen')
        user_dosen.profile.role = 'staff'

        user_mahasiswa = User.objects.create(username='mahasiswa',
                                             password='mahasiswa')
        user_mahasiswa.profile.role = 'mahasiswa'

        StatusSurat.objects.create(nama='lunas')
        StatusSurat.objects.create(nama='belum lunas')

    def test_request_not_authenticated(self):
        factory = APIRequestFactory()
        view = get_status_surat

        request = factory.get('/api/permohonan-surat/status-surat/')
        response = view(request)
        self.assertEqual(response.status_code, 401)

    def test_request_authenticated_admin(self):
        factory = APIRequestFactory()
        view = get_status_surat
        user = User.objects.get(username='admin')

        request = factory.get('/api/permohonan-surat/status-surat/')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_request_authenticated_dosen(self):
        factory = APIRequestFactory()
        view = get_status_surat
        user = User.objects.get(username='dosen')

        request = factory.get('/api/permohonan-surat/status-surat/')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 403)

    def test_request_authenticated_asdos(self):
        factory = APIRequestFactory()
        view = get_status_surat
        user = User.objects.get(username='asdos')

        request = factory.get('/api/permohonan-surat/status-surat/')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 403)

    def test_request_authenticated_alumni(self):
        factory = APIRequestFactory()
        view = get_status_surat
        user = User.objects.get(username='alumni')

        request = factory.get('/api/permohonan-surat/status-surat/')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 403)

    def test_request_authenticated_mahasiswa(self):
        factory = APIRequestFactory()
        view = get_status_surat
        user = User.objects.get(username='mahasiswa')

        request = factory.get('/api/permohonan-surat/status-surat/')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 403)
