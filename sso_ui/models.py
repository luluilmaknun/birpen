"""SSO UI models module."""
import json

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_cas_ng.signals import cas_user_authenticated

LANG = settings.SSO_UI_ORG_DETAIL_LANG
ORG_CODE = {}
with open(settings.SSO_UI_ORG_DETAIL_FILE_PATH, 'r') as ORG_CODE_FILE:
    ORG_CODE.update(json.load(ORG_CODE_FILE))


class User(AbstractUser):
    def is_admin(self):
        return Admin.objects.filter(username=self.username).exists()

    def is_asdos(self):
        return AsistenDosen.objects.filter(username=self.username).exists()

    def is_dosen(self):
        try:
            profile = self.profile
        except ObjectDoesNotExist:
            return False
        return profile.role == 'staff'

    def is_mahasiswa(self):
        try:
            profile = self.profile
        except ObjectDoesNotExist:
            return False

        return profile.role == 'mahasiswa'


class Admin(models.Model):
    username = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'admin'
        verbose_name_plural = verbose_name


class AsistenDosen(models.Model):
    username = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'asisten dosen'
        verbose_name_plural = verbose_name


class Profile(models.Model):
    """User Profile model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org_code = models.CharField('kode organisasi', max_length=11, blank=True)
    role = models.CharField('peran pengguna', max_length=128, blank=True)
    npm = models.CharField('Nomor Pokok Mahasiswa', max_length=10, blank=True)
    nip = models.CharField('Nomor Induk Pegawai', max_length=10, blank=True)
    faculty = models.CharField('fakultas', max_length=128, blank=True)
    study_program = models.CharField('program studi', max_length=128, blank=True)
    educational_program = models.CharField('program pendidikan', max_length=128, blank=True)

    class Meta:
        verbose_name = 'profil'
        verbose_name_plural = verbose_name

    def __str__(self):
        """Return username of the user."""
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """Create user profile if user object was just created."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(instance, **kwargs):
    """Save user profile post user save."""
    instance.profile.save()


@receiver(cas_user_authenticated)
def save_user_attributes(user, attributes, **kwargs):
    """Save user attributes from CAS into user and profile objects."""
    user.save()
    profile = user.profile
    profile.role = attributes['peran_user']

    if profile.role == 'staff':
        profile.nip = attributes['nip']

    if profile.role == 'mahasiswa':
        profile.npm = attributes['npm']

        org_code = attributes['kd_org']
        record = ORG_CODE[LANG][org_code]
        profile.org_code = org_code
        profile.faculty = record['faculty']
        profile.study_program = record['study_program']
        profile.educational_program = record['educational_program']

    user.email = f'{user.username}@ui.ac.id'

    full_name = attributes['nama']
    i = full_name.rfind(' ')
    user.first_name, user.last_name = full_name[:i], full_name[i + 1:]

    user.save()
