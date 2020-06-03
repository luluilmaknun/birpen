from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import DataKaryaAkhir

app = apps.get_app_config('karya_akhir')


class DisplayDataKaryaAkhir(admin.ModelAdmin):
    list_display = [field.name for field in DataKaryaAkhir._meta.get_fields()]
    list_filter = ['jenis_karya_akhir', ]


admin.site.register(DataKaryaAkhir, DisplayDataKaryaAkhir)


class DisplayNama(admin.ModelAdmin):
    list_display = ['nama']


for model_name, model in app.models.items():
    try:
        admin.site.register(model, DisplayNama)
    except AlreadyRegistered:
        continue
