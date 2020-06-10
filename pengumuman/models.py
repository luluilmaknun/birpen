# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from safedelete.models import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteModel


# For reference on using SafeDeleteModel please refer to
# https://github.com/makinacorpus/django-safedelete
#
# To summarize:
# - delete() behavior changed to soft delete
# - Use undelete() method to recover soft deleted object
# - Get all objects without soft deleted objects: Model.objects.all()
# - Get all objects with soft deleted objects: Model.all_objects.all()
# - Get soft deleted objects: Model.deleted_objects.all()

User = get_user_model()


class MataKuliah(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nama = models.CharField(max_length=32)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = 'mata kuliah'
        verbose_name_plural = verbose_name


class JenisPengumuman(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nama = models.CharField(max_length=32)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = 'jenis pengumuman'
        verbose_name_plural = verbose_name

class Ruang(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nama = models.CharField(max_length=32)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = 'ruang'
        verbose_name_plural = verbose_name


class Sesi(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nama = models.CharField(max_length=32)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = 'sesi'
        verbose_name_plural = verbose_name


class StatusPengumuman(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nama = models.CharField(max_length=32)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = 'status pengumuman'
        verbose_name_plural = verbose_name


class Pengumuman(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    tanggal_kelas = models.DateTimeField(default=timezone.now)
    pembuat = models.ForeignKey(User, on_delete=models.CASCADE)
    nama_mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    jenis_pengumuman = models.ForeignKey(JenisPengumuman, on_delete=models.CASCADE)
    nama_dosen = models.CharField(max_length=32)
    nama_asisten = models.CharField(max_length=32, blank=True, null=True)
    nama_ruang = models.ForeignKey(Ruang, on_delete=models.CASCADE)
    nama_sesi = models.ForeignKey(Sesi, on_delete=models.CASCADE)
    nama_status_pengumuman = models.ForeignKey(StatusPengumuman, on_delete=models.CASCADE)
    komentar = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'pengumuman'
        verbose_name_plural = verbose_name
