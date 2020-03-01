from django.db import models
from django.utils import timezone

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


# For reference on using SafeDeleteModel please refer to
# https://github.com/makinacorpus/django-safedelete
#
# To summarize:
# - delete() behavior changed to soft delete
# - Use undelete() method to recover soft deleted object
# - Get all objects without soft deleted objects: Model.objects.all()
# - Get all objects with soft deleted objects: Model.all_objects.all()
# - Get soft deleted objects: Model.deleted_objects.all()


class MataKuliah(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nama = models.CharField(max_length=32)


class JenisPengumuman(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nama = models.CharField(max_length=32)


class Ruang(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nama = models.CharField(max_length=32)


class Sesi(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nama = models.CharField(max_length=32)


class StatusPengumuman(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nama = models.CharField(max_length=32)


class Pengumuman(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    tanggal_kelas = models.DateTimeField(default=timezone.now)
    nama_pembuat = models.CharField(max_length=32)
    nama_mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    jenis_pengumuman = models.ForeignKey(JenisPengumuman, on_delete=models.CASCADE)
    nama_dosen = models.CharField(max_length=32)
    nama_asisten = models.CharField(max_length=32, blank=True)
    nama_ruang = models.ForeignKey(Ruang, on_delete=models.CASCADE)
    nama_sesi = models.ForeignKey(Sesi, on_delete=models.CASCADE)
    nama_status_pengumuman = models.ForeignKey(StatusPengumuman, on_delete=models.CASCADE)
    komentar = models.CharField(max_length=255, blank=True)
