from django.contrib.auth import get_user_model
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode
from django.test import TestCase

from rest_framework.test import APIClient

from rest_framework_jwt.settings import api_settings

from admin_birpen.models import Admin
from permohonan_surat.models import StatusBayar, StatusSurat, SuratAkademik, \
    Pesanan, PesananSuratAkademik

User = get_user_model()

class UpdateSuratTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user_admin = User.objects.create(username='min.admin', password='admin')
        Admin.objects.create(username=user_admin.username)
        self.token_admin = jwt_encode_handler(jwt_payload_handler(user_admin))

        user_mahasiswa = User.objects.create(username='muhammad.fauzan', password='not_admin')
        user_mahasiswa.profile.role = 'mahasiswa'
        self.token_mahasiswa = jwt_encode_handler(jwt_payload_handler(user_mahasiswa))

        user_alumni = User.objects.create(username='annida.safira', password='nida')
        user_alumni.profile.role = 'alumni'
        self.token_alumni = jwt_encode_handler(jwt_payload_handler(user_alumni))

        status_bayar_belom = StatusBayar.objects.create(nama="Belum Bayar")
        StatusBayar.objects.create(nama="Lunas")

        status_surat_proses = StatusSurat.objects.create(nama="Sedang diproses")
        StatusSurat.objects.create(nama="Selesai")

        surat_akademik = SuratAkademik.objects.create(
            jenis_dokumen="Surat Ket. Ijazah/Transkrip Hilang",
            harga_mahasiswa=0,
            harga_alumni=5000,
        )

        pesanan_mahasiswa = Pesanan.objects.create(
            nama_pemesan="muhammad fauzan",
            npm_pemesan="1707584930",
            waktu_pemesanan="2020-04-29T12:44:18Z",
            status_bayar=status_bayar_belom
        )

        pesanan_alumni = Pesanan.objects.create(
            nama_pemesan="annida safira",
            npm_pemesan="1703827383",
            waktu_pemesanan="2020-05-29T12:44:18Z",
            status_bayar=status_bayar_belom
        )

        pesanan_surat_akademik_mahasiswa = PesananSuratAkademik.objects.create(
            pesanan=pesanan_mahasiswa,
            surat_akademik=surat_akademik,
            status_surat=status_surat_proses,
            jumlah=1
        )
        self.pk_pesanan_surat_mahasiswa = pesanan_surat_akademik_mahasiswa.pk

        pesanan_surat_akademik_alumni = PesananSuratAkademik.objects.create(
            pesanan=pesanan_alumni,
            surat_akademik=surat_akademik,
            status_surat=status_surat_proses,
            jumlah=1
        )
        self.pk_pesanan_surat_alumni = pesanan_surat_akademik_alumni.pk

    def test_update_without_authentication(self):
        response = self.client.patch('/api/permohonan-surat/1/update-pesanan/',
                                     content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(response.status_code, 401)

    def test_surat_notfound(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.patch('/api/permohonan-surat/100/update-pesanan/',
                                     content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Surat/status tidak ditemukan.')
        self.assertEqual(response.status_code, 400)

    def test_status_bayar_notfound(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.patch(
            '/api/permohonan-surat/{}/update-pesanan/'.format(self.pk_pesanan_surat_mahasiswa),
            data=urlencode(MultiValueDict({
                'status_bayar': "Ngutang",
                'status_surat': "Selesai",
            })),
            content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Surat/status tidak ditemukan.')
        self.assertEqual(response.status_code, 400)

    def test_status_surat_notfound(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.patch(
            '/api/permohonan-surat/{}/update-pesanan/'.format(self.pk_pesanan_surat_mahasiswa),
            data=urlencode(MultiValueDict({
                'status_bayar': "Lunas",
                'status_surat': "Tunda",
            })),
            content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], 'Surat/status tidak ditemukan.')
        self.assertEqual(response.status_code, 400)

    def test_admin_success_update(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.patch(
            '/api/permohonan-surat/{}/update-pesanan/'.format(self.pk_pesanan_surat_mahasiswa),
            data=urlencode(MultiValueDict({
                'status_bayar': "Lunas",
                'status_surat': "Selesai",
            })),
            content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.status_code, 200)

    def test_mahasiswa_fail_update(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_mahasiswa)
        response = self.client.patch(
            '/api/permohonan-surat/{}/update-pesanan/'.format(self.pk_pesanan_surat_mahasiswa),
            data=urlencode(MultiValueDict({
                'status_bayar': "Lunas",
                'status_surat': "Selesai",
            })),
            content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], "Tidak memiliki hak untuk mengupdate surat.")
        self.assertEqual(response.status_code, 403)

    def test_alumni_fail_update(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_alumni)
        response = self.client.patch(
            '/api/permohonan-surat/{}/update-pesanan/'.format(self.pk_pesanan_surat_alumni),
            data=urlencode(MultiValueDict({
                'status_bayar': "Lunas",
                'status_surat': "Selesai",
            })),
            content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.data['detail'], "Tidak memiliki hak untuk mengupdate surat.")
        self.assertEqual(response.status_code, 403)
