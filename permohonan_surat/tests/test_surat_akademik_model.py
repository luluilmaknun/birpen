from django.contrib.auth import get_user_model
from django.test import TestCase
from django.db import IntegrityError

from permohonan_surat.models import SuratAkademik

User = get_user_model()


class SuratAkademikTest(TestCase):
    def setUp(self):
        self.surat = SuratAkademik.objects.create(jenis_dokumen="Transkrip nilai",
                                                  harga_mahasiswa=0, harga_alumni=10000)

        self.mahasiswa = User.objects.create(username='athallah.annafis',
                                             password='mahasiswa')
        self.mahasiswa.profile.role = 'mahasiswa'
        self.mahasiswa.profile.save()

        self.alumni = User.objects.create(username='annida.safira',
                                          password='alumni')
        self.alumni.profile.role = 'alumni'
        self.alumni.profile.save()

    def test_model_can_create(self):
        initial_count = SuratAkademik.objects.all().count()

        self.surat = SuratAkademik.objects.create(jenis_dokumen="Keterangan Kelakuan Baik",
                                                  harga_mahasiswa=0, harga_alumni=5000)

        count = SuratAkademik.objects.all().count()
        self.assertEqual(count, initial_count + 1)

    def test_model_not_create_with_invalid_data(self):
        with self.assertRaises(IntegrityError):
            SuratAkademik.objects.create(jenis_dokumen=None)

    def test_harga_according_user_role(self):
        self.assertEqual(self.surat.harga(self.mahasiswa), self.surat.harga_mahasiswa)
        self.assertEqual(self.surat.harga(self.alumni), self.surat.harga_alumni)
