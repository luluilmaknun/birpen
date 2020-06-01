from django.urls import path

from .views import karya_akhir_placeholder_views, read_surat_karya_akhir, \
    read_program_studi, read_mahasiswa_karya_akhir

urlpatterns = [
    path('', karya_akhir_placeholder_views, name='karya_akhir_placeholder_views'),
    path('surat/', read_surat_karya_akhir, name='read_surat_karya_akhir'),
    path('program-studi/', read_program_studi, name='read_program_studi'),
    path('mahasiswa/', read_mahasiswa_karya_akhir, name='read_mahasiswa_karya_akhir'),
]
