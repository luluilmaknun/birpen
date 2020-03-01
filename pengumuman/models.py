# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'mahasiswa'),
        (2, 'asdos'),
        (3, 'dosen'),
        (4, 'admin'),
    )
    name = models.CharField(max_length=50)
    npm = models.CharField(max_length=10)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
