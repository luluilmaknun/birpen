from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

User = get_user_model()


class PesanSuratAkademikTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        self.user_mahasiswa = User.objects.create(username="ahmad.fauzan", password="mahasiswa",
                                                  first_name="Ahmad", last_name="Fauzan")
        self.user_mahasiswa.profile.role = "mahasiswa"
        self.user_mahasiswa.profile.npm = "1706979923"
        self.user_mahasiswa.profile.save()
        self.token_mahasiswa = jwt_encode_handler(jwt_payload_handler(self.user_mahasiswa))

        user_alumni = User.objects.create(username="lulu.ilmaknun", password="alumni")
        user_alumni.profile.role = "alumni"
        user_alumni.profile.save()
        self.token_alumni = jwt_encode_handler(jwt_payload_handler(user_alumni))

        user_dosen = User.objects.create(username="yusuf.tri", password="dosen")
        self.token_dosen = jwt_encode_handler(jwt_payload_handler(user_dosen))
        user_dosen.profile.role = "staff"
        user_dosen.profile.save()

    def test_unauthorized_request_failed(self):
        response = self.client.get("/api/permohonan-surat/pesanan/mahasiswa-profile/")
        self.assertEqual(response.status_code, 401)

    def test_dosen_request_failed(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_dosen)
        response = self.client.get("/api/permohonan-surat/pesanan/mahasiswa-profile/")
        self.assertEqual(response.status_code, 403)

    def test_alumni_request_failed(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_alumni)
        response = self.client.get("/api/permohonan-surat/pesanan/mahasiswa-profile/")
        self.assertEqual(response.status_code, 403)

    def test_mahasiswa_request_success(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa)
        response = self.client.get("/api/permohonan-surat/pesanan/mahasiswa-profile/")
        self.assertEqual(response.status_code, 200)
        user_mahasiswa_full_name = self.user_mahasiswa.first_name + " " + \
                                   self.user_mahasiswa.last_name
        self.assertEqual(response.data['mahasiswa']['nama'], user_mahasiswa_full_name)
        self.assertEqual(response.data['mahasiswa']['npm'], self.user_mahasiswa.profile.npm)
