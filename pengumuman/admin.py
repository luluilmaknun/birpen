from django.apps import apps
from django.contrib import admin
from .models import MataKuliah, JenisPengumuman, Ruang, Sesi, StatusPengumuman,\
    Pengumuman

app = apps.get_app_config('pengumuman')

#for model_name, model in app.models.items():
#    admin.site.register(model)

class DisplayNama(admin.ModelAdmin):
    list_display = ['nama']

for model in [MataKuliah, JenisPengumuman, Ruang, Sesi, StatusPengumuman]:
    admin.site.register(model, DisplayNama)


class DisplayPengumuman(admin.ModelAdmin):
    list_display = [field.name for field in Pengumuman._meta.get_fields()]
    list_filter = ['tanggal_kelas', ]

admin.site.register(Pengumuman, DisplayPengumuman)

admin.site.site_header = "Halaman Admin Biro Pendidikan FEB UI"

