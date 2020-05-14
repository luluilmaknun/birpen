from django.apps import apps
from django.contrib import admin

from .models import Pesanan, PesananSuratAkademik, StatusBayar, StatusSurat, SuratAkademik

app = apps.get_app_config('permohonan_surat')

class DisplayNama(admin.ModelAdmin):
    list_display = ['nama']

class DisplaySuratAkademik(admin.ModelAdmin):
    list_display = ['jenis_dokumen', 'harga_mahasiswa', 'harga_alumni']

class DisplayPesanan(admin.ModelAdmin):
    list_display = [field.name for field in Pesanan._meta.get_fields()]

class DisplayPesananSuratAkademik(admin.ModelAdmin):
    list_display = [field.name for field in PesananSuratAkademik._meta.get_fields()]

for model in [StatusBayar, StatusSurat]:
    admin.site.register(model, DisplayNama)

admin.site.register(SuratAkademik, DisplaySuratAkademik)

admin.site.register(Pesanan, DisplayPesanan)

admin.site.register(PesananSuratAkademik, DisplayPesananSuratAkademik)
