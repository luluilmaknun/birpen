from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from karya_akhir.models import JenisKaryaAkhir, DataKaryaAkhir
from sso_ui.models import Admin

User = get_user_model()


class ReadMahasiswaKaryaAkhir(TestCase):
    def setUp(self):
        self.client = APIClient()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        jenis_karya_akhir_magang = JenisKaryaAkhir.objects.create(nama="Magang")

        self.user_mahasiswa_1 = User.objects.create(username="mahasiswa_1")
        self.user_mahasiswa_1.profile.role = "mahasiswa"
        self.user_mahasiswa_1.profile.save()
        self.token_mahasiswa_1 = jwt_encode_handler(jwt_payload_handler(self.user_mahasiswa_1))

        DataKaryaAkhir.objects.create(
            mahasiswa=self.user_mahasiswa_1,
            peminatan_mahasiswa="Akuntansi",
            jenis_karya_akhir=jenis_karya_akhir_magang,
            sks_diperoleh=147,
            pembimbing="Lulu Ilmaknun S.Ak",
            pembimbing_pendamping="Annida Safira S.Ak",
            judul_karya_id="Sebuah Judul",
            judul_karya_en="A Title"
        )

        self.user_admin = User.objects.create(username="admin")
        self.token_admin = jwt_encode_handler(jwt_payload_handler(self.user_admin))
        Admin.objects.create(username=self.user_admin.username)

        user_dosen = User.objects.create(username="dosen")
        self.token_dosen = jwt_encode_handler(jwt_payload_handler(user_dosen))
        user_dosen.profile.role = "staff"
        user_dosen.profile.save()

        user_alumni = User.objects.create(username="alumni")
        self.token_alumni = jwt_encode_handler(jwt_payload_handler(user_dosen))
        user_alumni.profile.role = "alumni"
        user_alumni.profile.save()

        self.mahasiswa_karya_akhir_1_response = [{
            "mahasiswa": {
                "username": self.user_mahasiswa_1.username,
                "nama": self.user_mahasiswa_1.first_name + ' ' + self.user_mahasiswa_1.last_name,
                "npm": self.user_mahasiswa_1.profile.npm,
                "program_studi": self.user_mahasiswa_1.profile.study_program,
                "angkatan": self.user_mahasiswa_1.profile.year_of_entry
            }
        }]

    def test_unauthorized_cant_read_mahassiwa_karya_akhir(self):
        response = self.client.get("/api/karya-akhir/mahasiswa/")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data['detail'],
                         "Authentication credentials were not provided.")

    def test_mahasiswa_cant_read_data_karya_akhir(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa_1)
        response = self.client.get("/api/karya-akhir/mahasiswa/")
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'],
                         "You do not have permission to perform this action.")

    def test_dosen_cant_read_data_karya_akhir(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_dosen)
        response = self.client.get("/api/karya-akhir/mahasiswa/")
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'],
                         "You do not have permission to perform this action.")

    def test_alumni_cant_read_data_karya_akhir(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_alumni)
        response = self.client.get("/api/karya-akhir/mahasiswa/")
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'],
                         "You do not have permission to perform this action.")

    def test_admin_can_read_data_karya_akhir(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_admin)
        response = self.client.get("/api/karya-akhir/mahasiswa/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['mahasiswa_karya_akhir'],
                         self.mahasiswa_karya_akhir_1_response)
