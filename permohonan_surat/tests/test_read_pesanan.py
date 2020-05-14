from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from admin_birpen.models import Admin
from permohonan_surat.models import StatusBayar, StatusSurat, SuratAkademik, \
    Pesanan, PesananSuratAkademik

User = get_user_model()


class ReadPesananTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user_admin = User.objects.create(username='min.admin', password='admin')
        Admin.objects.create(username=user_admin.username)
        self.token_admin = jwt_encode_handler(jwt_payload_handler(user_admin))

        user_mahasiswa = User.objects.create(username='muhammad.fauzan', password='not_admin')
        user_mahasiswa.profile.role = 'mahasiswa'
        user_mahasiswa.profile.save()
        self.token_mahasiswa = jwt_encode_handler(jwt_payload_handler(user_mahasiswa))

        user_alumni = User.objects.create(username='annida.safira', password='nida')
        user_alumni.profile.role = 'alumni'
        user_alumni.profile.save()
        self.token_alumni = jwt_encode_handler(jwt_payload_handler(user_alumni))

        user_dosen = User.objects.create(username='athallah.ahmad', password='dosen')
        user_dosen.profile.role = 'staff'
        user_dosen.profile.save()
        self.token_dosen = jwt_encode_handler(jwt_payload_handler(user_dosen))

        status_bayar_belom = StatusBayar.objects.create(nama="Belum Bayar")
        StatusBayar.objects.create(nama="Lunas")

        status_surat_proses = StatusSurat.objects.create(nama="Sedang diproses")
        status_surat_selesai = StatusSurat.objects.create(nama="Selesai")

        self.jenis_dokumen_1 = "Daftar Nilai Semester"
        self.jenis_dokumen_2 = "Legalisasi Transkrip Nilai"

        surat_akademik_1 = SuratAkademik.objects.create(
            jenis_dokumen=self.jenis_dokumen_1,
            harga_mahasiswa=0,
            harga_alumni=5000,
        )

        surat_akademik_2 = SuratAkademik.objects.create(
            jenis_dokumen=self.jenis_dokumen_2,
            harga_mahasiswa=0,
            harga_alumni=5000,
        )

        pesanan_mahasiswa = Pesanan.objects.create(
            pemesan=user_mahasiswa,
            nama_pemesan="muhammad fauzan",
            npm_pemesan="1707584930",
            waktu_pemesanan="2020-04-29T12:44:18Z",
            status_bayar=status_bayar_belom
        )
        self.id_pesanan_mahasiswa = pesanan_mahasiswa.pk

        pesanan_alumni = Pesanan.objects.create(
            pemesan=user_alumni,
            nama_pemesan="annida safira",
            npm_pemesan="1703827383",
            waktu_pemesanan="2020-05-29T12:44:18Z",
            status_bayar=status_bayar_belom
        )
        self.id_pesanan_alumni = pesanan_alumni.pk

        PesananSuratAkademik.objects.create(
            pesanan=pesanan_mahasiswa,
            surat_akademik=surat_akademik_1,
            status_surat=status_surat_proses,
            jumlah=1
        )
        PesananSuratAkademik.objects.create(
            pesanan=pesanan_mahasiswa,
            surat_akademik=surat_akademik_2,
            status_surat=status_surat_selesai,
            jumlah=3
        )

        PesananSuratAkademik.objects.create(
            pesanan=pesanan_alumni,
            surat_akademik=surat_akademik_2,
            status_surat=status_surat_proses,
            jumlah=3
        )

        self.api = '/api/permohonan-surat/'
        self.url_read = 'pesanan/'

    def test_read_without_authentication(self):
        url_request = self.api + self.url_read
        response = self.client.get(url_request, content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(response.status_code, 401)

    def test_output_admin_read_success(self):
        url_request = self.api + self.url_read
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.get(url_request, content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['pesanan']), 2)

    def test_output_mahasiswa_read_success(self):
        url_request = self.api + self.url_read
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_mahasiswa)
        response = self.client.get(url_request, content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['pesanan']), 1)

    def test_output_alumni_read_success(self):
        url_request = self.api + self.url_read
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_alumni)
        response = self.client.get(url_request, content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['pesanan']), 1)

    def test_output_dosen_read_fail(self):
        url_request = self.api + self.url_read
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_dosen)
        response = self.client.get(url_request, content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 403)
