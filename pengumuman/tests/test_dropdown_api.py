from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from pengumuman.models import MataKuliah, JenisPengumuman, Ruang, \
     Sesi, StatusPengumuman

from pengumuman.views import dropdown_pengumuman

User = get_user_model()


class DropdownApiTest(TestCase):
    def setUp(self):
        User.objects.create(username='julia.ningrum',
                            password='admin', is_admin=True)
        User.objects.create(username='yusuf.tri',
                            password='mahasiswa')

    def test_request_as_admin(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='julia.ningrum')
        view = dropdown_pengumuman

        JenisPengumuman.objects.create(nama='Asistensi')
        MataKuliah.objects.create(nama='Sistem Cerdas')
        Ruang.objects.create(nama='3111')
        Sesi.objects.create(nama='Sesi 1 (08.00 - 10.30)')
        StatusPengumuman.objects.create(nama='Terlambat')

        # Make an authenticated request to the view...
        request = factory.get('/api/pengumuman/dropdown')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)
