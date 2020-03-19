"""SSO UI tests module."""
import json

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.contrib.admin.sites import AdminSite

from django_cas_ng.signals import cas_user_authenticated

from .models import ORG_CODE, Profile
from .admin import ProfileAdmin

User = get_user_model()

class SSOUITest(TestCase):
    """Test SSO UI app."""

    class MockUser:
        pass

    class MockRequest():
        def __init__(self):
            self.user = SSOUITest.MockUser()

    ATTRIBUTES = {
        "nama": "Ice Bear",
        "peran_user": "mahasiswa",
        "npm": "1706123123",
        "kd_org": "01.00.12.01"
    }

    def setUp(self):
        """Set up test."""
        self.user = User.objects.create_superuser(
            username='username', password='password', email='username@test.com'
        )

    def test_login_url_exists(self):
        """Test if login url exists and redirects to CAS server (response code 302)."""
        response = self.client.get(reverse('sso_ui:login'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(settings.CAS_SERVER_URL))

    def test_logout_url_exists(self):
        """Test if logout url exists and redirects to CAS server (response code 302)."""
        response = self.client.get(reverse('sso_ui:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(settings.CAS_SERVER_URL))

    def test_profile_can_save_attributes(self):
        """Test if Profile model can save the attributes from CAS."""
        cas_user_authenticated.send(
            sender=self,
            user=self.user,
            created=False,
            attributes=SSOUITest.ATTRIBUTES
        )
        self.assertJSONEqual(
            json.dumps({
                "nama": self.user.get_full_name(),
                "peran_user": self.user.profile.role,
                "npm": self.user.profile.npm,
                "kd_org": self.user.profile.org_code
            }),
            SSOUITest.ATTRIBUTES
        )
        self.assertJSONEqual(
            json.dumps({
                "faculty": self.user.profile.faculty,
                "study_program": self.user.profile.study_program,
                "educational_program": self.user.profile.educational_program
            }),
            ORG_CODE['id'][SSOUITest.ATTRIBUTES['kd_org']]
        )
        self.assertEqual(self.user.email, f"{self.user.username}@ui.ac.id")
        self.assertEqual(self.user.first_name, "Ice")
        self.assertEqual(self.user.last_name, "Bear")

    def test_profile_str(self):
        """Test string representation of Profile model."""
        self.assertEqual(str(self.user.profile), self.user.username)

    def test_has_change_permission(self):
        """
        has_change_permission returns True for users who can edit objects and
        False for users who can't.
        """
        profile_admin = ProfileAdmin(Profile, AdminSite())
        request = self.MockRequest()

        self.assertFalse(profile_admin.has_change_permission(request))

    def test_success_create_token(self):
        user = User.objects.create_user(username='yusuf.tri',
                                        password='mahasiswa', user_type=User.MAHASISWA)
        self.client.force_login(user)
        response = self.client.get(reverse('sso_ui:create-token'))

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context['token'], '')

    def test_fail_create_token_user_not_authenticated(self):
        response = self.client.get(reverse('sso_ui:create-token'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['token'], '')
