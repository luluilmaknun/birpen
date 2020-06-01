from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from karya_akhir.models import JenisKaryaAkhir, DataKaryaAkhir
from sso_ui.models import Admin

User = get_user_model()


class FilterMahasiswaKaryaAkhir(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.jenis_karya_akhir = JenisKaryaAkhir.objects.create(nama="Skripsi")

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        self.user_mahasiswa_1, self.token_mahasiswa_1, self.data_karya_akhir_1 = \
            self.setup_mahasiswa("mahasiswa_1", "2016", "Akuntansi")
        self.user_mahasiswa_2, self.token_mahasiswa_2, self.data_karya_akhir_2 = \
            self.setup_mahasiswa("mahasiswa_2", "2016", "Bisnis Islam")
        self.user_mahasiswa_3, self.token_mahasiswa_3, self.data_karya_akhir_3 = \
            self.setup_mahasiswa("mahasiswa_3", "2017", "Ekonomi Islam")

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

    def setup_mahasiswa(self, nama, angkatan, prodi):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user_mahasiswa = User.objects.create(username=nama)
        user_mahasiswa.profile.role = "mahasiswa"
        user_mahasiswa.profile.year_of_entry = angkatan
        user_mahasiswa.profile.study_program = prodi
        user_mahasiswa.profile.save()
        token_mahasiswa = jwt_encode_handler(jwt_payload_handler(user_mahasiswa))

        data_karya_akhir = DataKaryaAkhir.objects.create(
            mahasiswa=user_mahasiswa,
            peminatan_mahasiswa="Akuntansi",
            jenis_karya_akhir=self.jenis_karya_akhir,
            sks_diperoleh=147,
            pembimbing="Lulu Ilmaknun S.Ak",
            pembimbing_pendamping="Annida Safira S.Ak",
            judul_karya_id="Sebuah Judul",
            judul_karya_en="A Title"
        )

        return user_mahasiswa, token_mahasiswa, data_karya_akhir

    def test_unauthorized_cant_filter_mahassiwa_karya_akhir(self):
        response = self.client \
            .get("/api/karya-akhir/filter-mahasiswa?angkatan=2016&prodi=Akuntansi")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data['detail'],
                         "Authentication credentials were not provided.")

    def test_mahasiswa_cant_filter_mahasiswa_karya_akhir(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa_1)
        response = self.client \
            .get("/api/karya-akhir/filter-mahasiswa?angkatan=2016&prodi=Akuntansi")
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'],
                         "You do not have permission to perform this action.")

    def test_dosen_cant_filter_mahasiswa_karya_akhir(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_dosen)
        response = self.client \
            .get("/api/karya-akhir/filter-mahasiswa?angkatan=2016&prodi=Akuntansi")
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'],
                         "You do not have permission to perform this action.")

    def test_alumni_cant_filter_mahasiswa_karya_akhir(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_alumni)
        response = self.client \
            .get("/api/karya-akhir/filter-mahasiswa?angkatan=2016&prodi=Akuntansi")
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'],
                         "You do not have permission to perform this action.")

    def test_admin_can_filter_mahasiswa_karya_akhir_angkatan_prodi(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_admin)
        expected_response = [{
            "mahasiswa": {
                "username": "mahasiswa_1",
                "nama": " ",
                "npm": "",
                "program_studi": "Akuntansi",
                "angkatan": "2016",
            }
        }]

        response = self.client \
            .get("/api/karya-akhir/filter-mahasiswa?angkatan=2016&prodi=Akuntansi")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['mahasiswa_karya_akhir'],
                         expected_response)

    def test_admin_can_filter_mahasiswa_karya_akhir_angkatan_only(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_admin)
        expected_response = [{
            "mahasiswa": {
                "username": "mahasiswa_3",
                "nama": " ",
                "npm": "",
                "program_studi": "Ekonomi Islam",
                "angkatan": "2017",
            }
        }]

        response = self.client \
            .get("/api/karya-akhir/filter-mahasiswa?angkatan=2017&prodi=")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['mahasiswa_karya_akhir'],
                         expected_response)

    def test_admin_can_filter_mahasiswa_karya_akhir_prodi_only(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_admin)
        expected_response = [{
            "mahasiswa": {
                "username": "mahasiswa_2",
                "nama": " ",
                "npm": "",
                "program_studi": "Bisnis Islam",
                "angkatan": "2016",
            }
        }]

        response = self.client \
            .get("/api/karya-akhir/filter-mahasiswa?angkatan=2016&prodi=Bisnis%20Islam")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['mahasiswa_karya_akhir'],
                         expected_response)

    def test_admin_can_filter_mahasiswa_karya_akhir_all(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_admin)
        expected_response = [
            {
                "mahasiswa": {
                    "username": "mahasiswa_1",
                    "nama": " ",
                    "npm": "",
                    "program_studi": "Akuntansi",
                    "angkatan": "2016",
               }
            },
            {
                "mahasiswa": {
                    "username": "mahasiswa_2",
                    "nama": " ",
                    "npm": "",
                    "program_studi": "Bisnis Islam",
                    "angkatan": "2016",
                }
            },
            {
                "mahasiswa": {
                    "username": "mahasiswa_3",
                    "nama": " ",
                    "npm": "",
                    "program_studi": "Ekonomi Islam",
                    "angkatan": "2017",
                }
            },
        ]

        response = self.client \
            .get("/api/karya-akhir/filter-mahasiswa?angkatan=&prodi=")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['mahasiswa_karya_akhir'],
                         expected_response)

    def test_admin_can_filter_mahasiswa_karya_akhir_none(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_admin)
        response = self.client \
            .get("/api/karya-akhir/filter-mahasiswa?angkatan=2018&prodi=Ekonomi")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['detail'], "Tidak ada data yang tersedia")
