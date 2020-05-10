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
    pemesan = models.ForeignKey(User, on_delete=models.CASCADE)
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
