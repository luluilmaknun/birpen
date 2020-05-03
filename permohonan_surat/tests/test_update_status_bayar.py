from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from permohonan_surat.models import StatusBayar, SuratAkademik, Pesanan
from admin_birpen.models import Admin

User = get_user_model()


class UpdateStatusBayarTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user_admin = User.objects.create(username="lulu.ilmaknun", password="admin")
        Admin.objects.create(username=user_admin.username)
        self.token_admin = jwt_encode_handler(jwt_payload_handler(user_admin))

        user_non_admin = User.objects.create(username="ahmad.fauzan", password="nonadmin")
        self.token_non_admin = jwt_encode_handler(jwt_payload_handler(user_non_admin))

        self.status_belum_bayar = StatusBayar.objects.create(nama="Belum Bayar")
        self.status_lunas = StatusBayar.objects.create(nama="Lunas")

        self.academic_letter_1 = SuratAkademik.objects.create(
            jenis_dokumen="Surat Keterangan Mahasiswa",
            harga_mahasiswa=0, harga_alumni=5000
        )

        self.academic_letter_2 = SuratAkademik.objects.create(
            jenis_dokumen="Daftar Nilai Semester",
            harga_mahasiswa=0, harga_alumni=5000
        )

        self.pesanan = Pesanan.objects.create(pk=1, pemesan=user_non_admin,
                                              nama_pemesan="Ahmad Fauzan",
                                              npm_pemesan=1706979322,
                                              status_bayar=self.status_belum_bayar)

        self.invalid_pesanan_id = 100
        self.invalid_status_bayar = "Ngutang"

    def test_unauthorized_request_cant_update_status_bayar(self):
        response = self.client.patch("/api/permohonan-surat/pesanan/" +
                                     str(self.pesanan.pk) + "/update-status-bayar/",
                                     data={"status_bayar": self.status_lunas.nama}, format="json")
        self.assertEqual(response.status_code, 401)

    def test_non_admin_cant_update_status_bayar(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_non_admin)
        response = self.client.patch("/api/permohonan-surat/pesanan/" +
                                     str(self.pesanan.pk) + "/update-status-bayar/",
                                     data={"status_bayar": self.status_lunas.nama}, format="json")
        self.assertEqual(response.status_code, 403)

    def test_pesanan_not_found(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_admin)
        response = self.client.patch("/api/permohonan-surat/pesanan/" +
                                     str(self.invalid_pesanan_id) + "/update-status-bayar/",
                                     data={"status_bayar": self.status_lunas.nama}, format="json")
        self.assertEqual(response.data['detail'], 'Data pesanan tidak ditemukan.')
        self.assertEqual(response.status_code, 400)

    def test_status_bayar_not_found(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_admin)
        response = self.client.patch("/api/permohonan-surat/pesanan/" +
                                     str(self.pesanan.pk) + "/update-status-bayar/",
                                     data={"status_bayar": self.invalid_status_bayar},
                                     format="json")
        self.assertEqual(response.data['detail'], 'Data status bayar tidak ditemukan.')
        self.assertEqual(response.status_code, 400)

    def test_status_bayar_not_provided(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_admin)
        response = self.client.patch("/api/permohonan-surat/pesanan/" +
                                     str(self.pesanan.pk) + "/update-status-bayar/",
                                     data={}, format="json")
        self.assertEqual(response.data['detail'], 'Data status bayar tidak ditemukan.')
        self.assertEqual(response.status_code, 400)

    def test_success_update_status_bayar(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token_admin)
        response = self.client.patch("/api/permohonan-surat/pesanan/" +
                                     str(self.pesanan.pk) + "/update-status-bayar/",
                                     data={"status_bayar": self.status_lunas.nama}, format="json")
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.status_code, 200)
