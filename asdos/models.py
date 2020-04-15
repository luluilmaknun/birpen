from django.db import models


class AsistenDosen(models.Model):
    username = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'asisten dosen'
        verbose_name_plural = verbose_name
