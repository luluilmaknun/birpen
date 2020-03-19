from django.contrib.auth import get_user_model
from django.test import TestCase

from sso_ui.models import Admin, AsistenDosen

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

    def test_is_admin_return_true_for_admin(self):
        self.assertTrue(self.user_admin.is_admin())

    def test_is_admin_return_false_for_non_admin(self):
        self.assertFalse(self.user.is_admin())

    def test_is_asdos_return_true_for_asisten_dosen(self):
        self.assertTrue(self.user_asisten_dosen.is_asdos())

    def test_is_asdos_return_false_for_non_asisten_dosen(self):
        self.assertFalse(self.user.is_asdos())
