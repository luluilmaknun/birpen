from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import Pengumuman

app = apps.get_app_config('pengumuman')

# for model_name, model in app.models.items():
#    admin.site.register(model)

admin.site.site_header = "Halaman Admin Biro Pendidikan FEB UI"


class DisplayPengumuman(admin.ModelAdmin):
    list_display = [field.name for field in Pengumuman._meta.get_fields()]
    list_filter = ['tanggal_kelas', ]


admin.site.register(Pengumuman, DisplayPengumuman)


class DisplayNama(admin.ModelAdmin):
    list_display = ['nama']


for model_name, model in app.models.items():
    try:
        admin.site.register(model, DisplayNama)
    except AlreadyRegistered:
        continue
