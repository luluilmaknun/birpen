from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from permohonan_surat.models import StatusSurat, StatusBayar, SuratAkademik

User = get_user_model()


class PesanSuratAkademikTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user_mahasiswa = User.objects.create(username="ahmad.fauzan", password="mahasiswa")
        user_mahasiswa.profile.role = "mahasiswa"
        user_mahasiswa.profile.save()
        self.token_mahasiswa = jwt_encode_handler(jwt_payload_handler(user_mahasiswa))

        user_alumni = User.objects.create(username="lulu.ilmaknun", password="alumni")
        user_alumni.profile.role = "alumni"
        user_alumni.profile.save()
        self.token_alumni = jwt_encode_handler(jwt_payload_handler(user_alumni))

        user_dosen = User.objects.create(username="yusuf.tri", password="dosen")
        self.token_dosen = jwt_encode_handler(jwt_payload_handler(user_dosen))
        user_dosen.profile.role = "staff"
        user_dosen.profile.save()

        StatusSurat.objects.create(pk=1, nama="Sedang Diproses")
        StatusBayar.objects.create(pk=1, nama="Belum Bayar")

        self.academic_letter_1 = SuratAkademik.objects.create(
            jenis_dokumen="Surat Keterangan Mahasiswa",
            harga_mahasiswa=0, harga_alumni=5000
        )

        self.academic_letter_2 = SuratAkademik.objects.create(
            jenis_dokumen="Daftar Nilai Semester",
            harga_mahasiswa=0, harga_alumni=5000
        )

        self.valid_data = {
            "nama_pemesan": "Ahmad Fauzan",
            "npm_pemesan": "1706979921",
            "surat_akademik" : [
                {
                    "jenis_dokumen": "Surat Keterangan Mahasiswa",
                    "jumlah": 2
                },
                {
                    "jenis_dokumen": "Daftar Nilai Semester",
                    "jumlah": 1
                }
            ]
        }

        self.valid_data_mahasiswa = {
            "surat_akademik" : [
                {
                    "jenis_dokumen": "Surat Keterangan Mahasiswa",
                    "jumlah": 2
                },
                {
                    "jenis_dokumen": "Daftar Nilai Semester",
                    "jumlah": 1
                }
            ]
        }

    def test_unauthorized_request_cant_create_academic_letter(self):
        response = self.client.post("/api/permohonan-surat/pesanan/create/",
                                    data=self.valid_data, format="json")
        self.assertEqual(response.status_code, 401)

    def test_dosen_cant_create_academic_letter(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_dosen)
        response = self.client.post("/api/permohonan-surat/pesanan/create/",
                                    data=self.valid_data, format="json")
        self.assertEqual(response.status_code, 403)

    def test_nama_alumni_pemesan_not_provided(self):
        data = {
            "npm_pemesan": "1706979921",
            "surat_akademik" : [
                {
                    "jenis_dokumen": "Surat Keterangan Mahasiswa",
                    "jumlah": 2
                },
                {
                    "jenis_dokumen": "Daftar Nilai Semester",
                    "jumlah": 1
                }
            ]
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_alumni)
        response = self.client.post("/api/permohonan-surat/pesanan/create/",
                                    data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_npm_alumni_pemesan_not_provided(self):
        data = {
            "npm_pemesan": "1706979921",
            "surat_akademik" : [
                {
                    "jenis_dokumen": "Surat Keterangan Mahasiswa",
                    "jumlah": 2
                },
                {
                    "jenis_dokumen": "Daftar Nilai Semester",
                    "jumlah": 1
                }
            ]
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_alumni)
        response = self.client.post("/api/permohonan-surat/pesanan/create/",
                                    data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_surat_akademik_not_provided(self):
        data = {
            "nama_pemesan": "Ahmad Fauzan",
            "npm_pemesan": "1706979921",
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa)
        response = self.client.post("/api/permohonan-surat/pesanan/create/",
                                    data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_jenis_dokumen_surat_akademik_not_provided(self):
        data = {
            "nama_pemesan": "Ahmad Fauzan",
            "npm_pemesan": "1706979921",
            "surat_akademik" : [
                {
                    "jumlah": 0
                },
                {
                    "jenis_dokumen": "Daftar Nilai Semester",
                    "jumlah": 1
                }
            ]
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa)
        response = self.client.post("/api/permohonan-surat/pesanan/create/",
                                    data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_jumlah_surat_akademik_not_provided(self):
        data = {
            "nama_pemesan": "Ahmad Fauzan",
            "npm_pemesan": "1706979921",
            "surat_akademik" : [
                {
                    "jenis_dokumen": "Surat Keterangan Mahasiswa",
                },
                {
                    "jenis_dokumen": "Daftar Nilai Semester",
                    "jumlah": 1
                }
            ]
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa)
        response = self.client.post("/api/permohonan-surat/pesanan/create/",
                                    data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_nama_pemesan_alumni_exceed_max_length(self):
        data = {
            "nama_pemesan": "A"*65,
            "npm_pemesan": "1706979921",
            "surat_akademik" : [
                {
                    "jenis_dokumen": "Surat Keterangan Mahasiswa",
                    "jumlah": 2
                },
                {
                    "jenis_dokumen": "Daftar Nilai Semester",
                    "jumlah": 1
                }
            ]
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_alumni)
        response = self.client.post("/api/permohonan-surat/pesanan/create/",
                                    data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_npm_pemesan_alumni_exceed_max_length(self):
        data = {
            "nama_pemesan": "Ahmad Fauzan",
            "npm_pemesan": "1"*11,
            "surat_akademik" : [
                {
                    "jenis_dokumen": "Surat Keterangan Mahasiswa",
                    "jumlah": 2
                },
                {
                    "jenis_dokumen": "Daftar Nilai Semester",
                    "jumlah": 1
                }
            ]
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_alumni)
        response = self.client.post("/api/permohonan-surat/pesanan/create/",
                                    data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_surat_akademik_not_found(self):
        data = {
            "nama_pemesan": "Ahmad Fauzan",
            "npm_pemesan": "1706979921",
            "surat_akademik" : [
                {
                    "jenis_dokumen": "Surat Keterangan Lulus",
                    "jumlah": 2
                },
                {
                    "jenis_dokumen": "Daftar Nilai Semester",
                    "jumlah": 1
                }
            ]
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa)
        response = self.client.post("/api/permohonan-surat/pesanan/create/",
                                    data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_jumlah_surat_akademik_cant_be_zero(self):
        data = {
            "nama_pemesan": "Ahmad Fauzan",
            "npm_pemesan": "1706979921",
            "surat_akademik" : [
                {
                    "jenis_dokumen": "Surat Keterangan Mahasiswa",
                    "jumlah": 0
                },
                {
                    "jenis_dokumen": "Daftar Nilai Semester",
                    "jumlah": 1
                }
            ]
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa)
        response = self.client.post("/api/permohonan-surat/pesanan/create/",
                                    data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_jumlah_surat_akademik_cant_be_negative(self):
        data = {
            "nama_pemesan": "Ahmad Fauzan",
            "npm_pemesan": "1706979921",
            "surat_akademik" : [
                {
                    "jenis_dokumen": "Surat Keterangan Mahasiswa",
                    "jumlah": -1
                },
                {
                    "jenis_dokumen": "Daftar Nilai Semester",
                    "jumlah": 1
                }
            ]
        }

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa)
        response = self.client.post("/api/permohonan-surat/pesanan/create/",
                                    data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_mahasiswa_can_create_surat_akademik(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_mahasiswa)
        response = self.client.post("/api/permohonan-surat/pesanan/create/",
                                    data=self.valid_data_mahasiswa, format="json")
        self.assertEqual(response.status_code, 200)

    def test_alumni_can_create_surat_akademik(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_alumni)
        response = self.client.post("/api/permohonan-surat/pesanan/create/",
                                    data=self.valid_data, format="json")
        self.assertEqual(response.status_code, 200)
