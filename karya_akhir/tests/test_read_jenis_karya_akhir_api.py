from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from karya_akhir.models import JenisKaryaAkhir
from karya_akhir.views import read_jenis_karya_akhir

from sso_ui.models import Admin

User = get_user_model()


class ReadSuratKaryaAkhirApiTest(TestCase):
    def setUp(self):
        self.user_admin = User.objects.create(username='admin',
                                              password='admin')
        Admin.objects.create(username=self.user_admin.username)

        self.user_alumni = User.objects.create(username='alumni',
                                               password='alumni')
        self.user_alumni.profile.role = 'alumni'
        self.user_alumni.profile.save()

        self.user_dosen = User.objects.create(username='dosen',
                                              password='dosen')
        self.user_dosen.profile.role = 'staff'
        self.user_dosen.profile.save()

        self.user_mahasiswa = User.objects.create(username='mahasiswa',
                                                  password='mahasiswa')
        self.user_mahasiswa.profile.role = 'mahasiswa'
        self.user_mahasiswa.profile.save()

        JenisKaryaAkhir.objects.create(nama='Skripsi')
        JenisKaryaAkhir.objects.create(nama='Tugas Akhir')

    def test_request_unauthenticated_failed(self):
        factory = APIRequestFactory()
        view = read_jenis_karya_akhir

        request = factory.get('/api/karya-akhir/jenis-karya-akhir/')
        response = view(request)
        self.assertEqual(response.status_code, 401)

    def test_request_as_dosen_failed(self):
        factory = APIRequestFactory()
        view = read_jenis_karya_akhir

        request = factory.get('/api/karya-akhir/jenis-karya-akhir/')
        force_authenticate(request, user=self.user_dosen)
        response = view(request)
        self.assertEqual(response.status_code, 403)

    def test_request_as_alumni_failed(self):
        factory = APIRequestFactory()
        view = read_jenis_karya_akhir

        request = factory.get('/api/karya-akhir/jenis-karya-akhir/')
        force_authenticate(request, user=self.user_alumni)
        response = view(request)
        self.assertEqual(response.status_code, 403)

    def test_request_as_mahasiswa_success(self):
        factory = APIRequestFactory()
        view = read_jenis_karya_akhir

        request = factory.get('/api/karya-akhir/jenis-karya-akhir/')
        force_authenticate(request, user=self.user_mahasiswa)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_request_as_admin_success(self):
        factory = APIRequestFactory()
        view = read_jenis_karya_akhir

        request = factory.get('/api/karya-akhir/jenis-karya-akhir/')
        force_authenticate(request, user=self.user_admin)
        response = view(request)
        self.assertEqual(response.status_code, 200)
