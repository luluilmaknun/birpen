from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from karya_akhir.models import JenisKaryaAkhir, DataKaryaAkhir

User = get_user_model()


class CreateDataKaryaAkhirTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user_mahasiswa = User.objects.create(username="ahmad.fauzan", password="mahasiswa")
        user_mahasiswa.profile.role = "mahasiswa"
        user_mahasiswa.profile.save()
        self.token_mahasiswa = jwt_encode_handler(jwt_payload_handler(user_mahasiswa))

        user_mahasiswa_without_data_karya_akhir = \
            User.objects.create(username="athallah.annafis", password="mahasiswa")
        user_mahasiswa_without_data_karya_akhir.profile.role = "mahasiswa"
        user_mahasiswa_without_data_karya_akhir.profile.save()
        self.token_mahasiswa_without_data_karya_akhir = \
            jwt_encode_handler(jwt_payload_handler(user_mahasiswa_without_data_karya_akhir))

        user_alumni = User.objects.create(username="lulu.ilmaknun", password="alumni")
        user_alumni.profile.role = "alumni"
        user_alumni.profile.save()
        self.token_alumni = jwt_encode_handler(jwt_payload_handler(user_alumni))

        user_dosen = User.objects.create(username="yusuf.tri", password="dosen")
        self.token_dosen = jwt_encode_handler(jwt_payload_handler(user_dosen))
        user_dosen.profile.role = "staff"
        user_dosen.profile.save()

        self.jenis_karya_akhir_skripsi = JenisKaryaAkhir.objects.create(nama="Skripsi")
        self.jenis_karya_akhir_magang = JenisKaryaAkhir.objects.create(nama="Magang")
        self.invalid_nama_jenis_karya_akhir = "Invalid Nama Jenis Karya Akhir"

        DataKaryaAkhir.objects.create(
            mahasiswa=user_mahasiswa,
            peminatan_mahasiswa="Akuntansi",
            jenis_karya_akhir=self.jenis_karya_akhir_magang,
            sks_diperoleh=147,
            pembimbing="Lulu Ilmaknun S.Ak",
            pembimbing_pendamping="Annida Safira S.Ak",
            judul_karya_id="Sebuah Judul",
            judul_karya_en="A Title"
        )

        self.valid_data = {
            "peminatan_mahasiswa": "Akuntansi Islam",
            "jenis_karya_akhir": self.jenis_karya_akhir_skripsi.nama,
            "sks_diperoleh": 144,
            "pembimbing": "Ahmad Fauzan S.Ak",
            "pembimbing_pendamping": "Yusuf Tri S.Ak",
            "judul_karya_id": "Sebuah Karya",
            "judul_karya_en": "A Masterpiece"
        }

    def test_unauthorized_request_cant_create_data_karya_akhir(self):
        response = self.client.put("/api/karya-akhir/edit/",
                                   data=self.valid_data, format="json")
        self.assertEqual(response.status_code, 401)

    def test_dosen_cant_create_data_karya_akhir(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_dosen)
        response = self.client.put("/api/karya-akhir/edit/",
                                   data=self.valid_data, format="json")
        self.assertEqual(response.status_code, 403)

    def test_alumni_cant_create_data_karya_akhir(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_alumni)
        response = self.client.put("/api/karya-akhir/edit/",
                                   data=self.valid_data, format="json")
        self.assertEqual(response.status_code, 403)

    def test_required_data_not_provided(self):
        data = {
            "jenis_karya_akhir": self.jenis_karya_akhir_skripsi.nama,
            "sks_diperoleh": 144,
            "pembimbing": "Ahmad Fauzan S.Ak",
            "pembimbing_pendamping": "Yusuf Tri S.Ak",
            "judul_karya_id": "Sebuah Karya",
            "judul_karya_en": "A Masterpiece"
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa)
        response = self.client.put("/api/karya-akhir/edit/",
                                   data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_data_exceed_max_length(self):
        data = {
            "peminatan_mahasiswa": "A"*101,
            "jenis_karya_akhir": self.jenis_karya_akhir_skripsi.nama,
            "sks_diperoleh": 144,
            "pembimbing": "Ahmad Fauzan S.Ak",
            "pembimbing_pendamping": "Yusuf Tri S.Ak",
            "judul_karya_id": "Sebuah Karya",
            "judul_karya_en": "A Masterpiece"
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa)
        response = self.client.put("/api/karya-akhir/edit/",
                                   data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_invalid_data_type(self):
        data = {
            "peminatan_mahasiswa": "Akuntansi Islam",
            "jenis_karya_akhir": self.jenis_karya_akhir_skripsi.nama,
            "sks_diperoleh": "A",
            "pembimbing": "Ahmad Fauzan S.Ak",
            "pembimbing_pendamping": "Yusuf Tri S.Ak",
            "judul_karya_id": "Sebuah Karya",
            "judul_karya_en": "A Masterpiece"
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa)
        response = self.client.put("/api/karya-akhir/edit/",
                                   data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_jenis_karya_akhir_not_found(self):
        data = {
            "peminatan_mahasiswa": "A"*101,
            "jenis_karya_akhir": self.invalid_nama_jenis_karya_akhir,
            "sks_diperoleh": 144,
            "pembimbing": "Ahmad Fauzan S.Ak",
            "pembimbing_pendamping": "Yusuf Tri S.Ak",
            "judul_karya_id": "Sebuah Karya",
            "judul_karya_en": "A Masterpiece"
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa)
        response = self.client.put("/api/karya-akhir/edit/",
                                   data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_sks_diperoleh_cant_be_negative(self):
        data = {
            "peminatan_mahasiswa": "Akuntansi Islam",
            "jenis_karya_akhir": self.invalid_nama_jenis_karya_akhir,
            "sks_diperoleh": -1,
            "pembimbing": "Ahmad Fauzan S.Ak",
            "pembimbing_pendamping": "Yusuf Tri S.Ak",
            "judul_karya_id": "Sebuah Karya",
            "judul_karya_en": "A Masterpiece"
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa)
        response = self.client.put("/api/karya-akhir/edit/",
                                   data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_failed_to_edit_if_mahasiswa_not_has_data_karya_akhir(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + \
                                self.token_mahasiswa_without_data_karya_akhir)
        response = self.client.put("/api/karya-akhir/edit/",
                                   data=self.valid_data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_mahasiswa_can_create_surat_akademik(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa)
        response = self.client.put("/api/karya-akhir/edit/",
                                   data=self.valid_data, format="json")
        self.assertEqual(response.status_code, 200)
