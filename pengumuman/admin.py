from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from .models import User
from .apps import PengumumanConfig

app = apps.get_app_config('pengumuman')

for model_name, model in app.models.items():
    admin.site.register(model)
