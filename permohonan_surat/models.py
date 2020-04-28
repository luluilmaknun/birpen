from django.db import models


class StatusBayar(models.Model):
    nama = models.CharField(max_length=64, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = 'status bayar'
        verbose_name_plural = verbose_name


class StatusSurat(models.Model):
    nama = models.CharField(max_length=64, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = 'status surat'
        verbose_name_plural = verbose_name
