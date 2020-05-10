from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ProgramStudi(models.Model):
    """
    Used for listing study program, in case need of study program list
    """
    nama = models.CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = 'program studi'
        verbose_name_plural = verbose_name


class SuratKaryaAkhir(models.Model):
    nama = models.CharField(max_length=100, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = 'surat karya akhir'
        verbose_name_plural = verbose_name


class JenisKaryaAkhir(models.Model):
    nama = models.CharField(max_length=20, null=False, blank=False, unique=True)
    class Meta:
        verbose_name = 'jenis karya akhir'
        verbose_name_plural = verbose_name


class DataKaryaAkhir(models.Model):
    mahasiswa = models.ForeignKey(User, on_delete=models.CASCADE)
    peminatan_mahasiswa = models.CharField(max_length=100, null=False, blank=False)
    jenis_karya_akhir = models.ForeignKey(JenisKaryaAkhir, on_delete=models.CASCADE)
    sks_diperoleh = models.PositiveIntegerField(null=False, blank=False)
    pembimbing = models.CharField(max_length=70, null=False, blank=False)
    pembimbing_pendamping = models.CharField(max_length=70, blank=True)
    judul_karya_id = models.TextField(null=False, blank=False)
    judul_karya_en = models.TextField(blank=True)

    class Meta:
        verbose_name = 'data karya akhir'
        verbose_name_plural = verbose_name
