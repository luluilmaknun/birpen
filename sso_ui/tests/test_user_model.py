from django.contrib.auth import get_user_model
from django.test import TestCase

from asdos.models import AsistenDosen
from admin_birpen.models import Admin

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='athallah.annafis',
                                        password='mahasiswa')

        self.user_admin = User.objects.create(username='julia.ningrum',
                                              password='admin')
        Admin.objects.create(username=self.user_admin.username)

        self.user_asisten_dosen = User.objects.create(username='yusuf.tri',
                                                      password='asdos')
        AsistenDosen.objects.create(username=self.user_asisten_dosen.username)

        self.user_without_profile = User.objects.create(username='lulu.ilmaknun',
                                                        password='lulu')
        self.user_without_profile.profile.delete()
        self.user_without_profile.refresh_from_db()

        self.user_mahasiswa = User.objects.create(username='annida.safira',
                                                  password='nida')
        self.user_mahasiswa.profile.role = 'mahasiswa'
        self.user_mahasiswa.profile.save()

        self.user_dosen = User.objects.create(username='ahmad.fauzan',
                                              password='fauzan')
        self.user_dosen.profile.role = 'staff'
        self.user_dosen.profile.save()

        self.user_alumni = User.objects.create(username='agas.yanpratama',
                                               password='agas')
        self.user_alumni.profile.role = 'alumni'
        self.user_alumni.profile.save()

    def test_is_admin_return_true_for_admin(self):
        self.assertTrue(self.user_admin.is_admin())

    def test_is_admin_return_false_for_non_admin(self):
        self.assertFalse(self.user.is_admin())

    def test_is_asdos_return_true_for_asisten_dosen(self):
        self.assertTrue(self.user_asisten_dosen.is_asdos())

    def test_is_asdos_return_false_for_non_asisten_dosen(self):
        self.assertFalse(self.user.is_asdos())

    def test_is_mahasiswa_return_true_for_mahasiswa(self):
        self.assertTrue(self.user_mahasiswa.is_mahasiswa())

    def test_is_mahasiswa_return_false_for_non_mahasiswa(self):
        self.assertFalse(self.user.is_mahasiswa())

    def test_is_mahasiswa_return_false_if_no_profile(self):
        self.assertFalse(self.user_without_profile.is_mahasiswa())

    def test_is_dosen_return_true_for_dosen(self):
        self.assertTrue(self.user_dosen.is_dosen())

    def test_is_dosen_return_false_for_non_dosen(self):
        self.assertFalse(self.user.is_dosen())

    def test_is_dosen_return_false_if_no_profile(self):
        self.assertFalse(self.user_without_profile.is_dosen())

    def test_is_alumni_return_true_for_alumni(self):
        self.assertTrue(self.user_alumni.is_alumni())

    def test_is_alumni_return_false_for_non_alumni(self):
        self.assertFalse(self.user.is_alumni())

    def test_is_alumni_return_false_if_no_profile(self):
        self.assertFalse(self.user_without_profile.is_alumni())
