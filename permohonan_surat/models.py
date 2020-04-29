from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator

User = get_user_model()

DEFAULT_STATUS_BAYAR = 1
DEFAULT_STATUS_SURAT = 1

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


class SuratAkademik(models.Model):
    jenis_dokumen = models.CharField(max_length=64, null=False, blank=False, unique=True)
    harga_mahasiswa = models.PositiveIntegerField(null=False, blank=False, default=0)
    harga_alumni = models.PositiveIntegerField(null=False, blank=False, default=0)

    class Meta:
        verbose_name = 'surat akademik'
        verbose_name_plural = verbose_name

    def harga(self, user):
        if user.is_mahasiswa():
            return self.harga_mahasiswa
        return self.harga_alumni


class Pesanan(models.Model):
    nama_pemesan = models.CharField(max_length=64)
    npm_pemesan = models.CharField(max_length=10)
    waktu_pemesanan = models.DateTimeField(auto_now_add=True)
    status_bayar = models.ForeignKey(StatusBayar, on_delete=models.CASCADE,
                                     default=DEFAULT_STATUS_BAYAR)

    class Meta:
        verbose_name = 'pesanan'
        verbose_name_plural = verbose_name


class PesananSuratAkademik(models.Model):
    pesanan = models.ForeignKey(Pesanan, on_delete=models.CASCADE)
    surat_akademik = models.ForeignKey(SuratAkademik, on_delete=models.CASCADE)
    status_surat = models.ForeignKey(StatusSurat, on_delete=models.CASCADE,
                                     default=DEFAULT_STATUS_SURAT)
    jumlah = models.PositiveIntegerField(null=False, blank=False,
                                         validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = 'pesanan surat akademik'
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(fields=['pesanan', 'surat_akademik'],
                                    name='Unique combination pesanan and surat_akademik')
        ]
